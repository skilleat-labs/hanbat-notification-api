from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import time

app = FastAPI(title="한밭푸드 알림 서비스")

# 주문 상태 메시지 매핑
STATUS_MESSAGES = {
    "주문접수": "주문이 접수되었습니다. 곧 처리될 예정입니다.",
    "결제완료": "결제가 완료되었습니다. 상품을 준비 중입니다.",
    "배송중":   "상품이 출발했습니다. 빠르게 배달해드리겠습니다.",
    "배송완료": "배송이 완료되었습니다. 감사합니다!",
    "취소":     "주문이 취소되었습니다.",
}

# 샘플 주문 데이터
ORDERS = {
    "ORD-001": {"status": "배송완료", "product": "유기농 쌀 10kg", "user": "김철수"},
    "ORD-002": {"status": "배송중",   "product": "제주 감귤 5kg",  "user": "이영희"},
    "ORD-003": {"status": "결제완료", "product": "국내산 돼지고기", "user": "박민준"},
}


class NotificationResponse(BaseModel):
    order_id: str
    user: str
    product: str
    status: str
    message: str
    sent_at: float


@app.get("/health")
async def health():
    return {"status": "ok", "service": "notification-api"}


@app.get("/api/notify/{order_id}", response_model=NotificationResponse)
async def notify(order_id: str):
    order = ORDERS.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"주문 {order_id}을 찾을 수 없습니다.")

    message = STATUS_MESSAGES.get(order["status"], "주문 상태가 업데이트되었습니다.")

    return NotificationResponse(
        order_id=order_id,
        user=order["user"],
        product=order["product"],
        status=order["status"],
        message=message,
        sent_at=time.time(),
    )


@app.get("/api/notify")
async def list_notifications():
    return [
        {
            "order_id": oid,
            "user": o["user"],
            "status": o["status"],
            "message": STATUS_MESSAGES.get(o["status"], ""),
        }
        for oid, o in ORDERS.items()
    ]
