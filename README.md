# hanbat-notification-api

한밭푸드 알림 서비스 — Composable Architecture 운영 자동화 평가용 레포

## 평가 과제

이 레포를 Fork하여 아래 파이프라인을 처음부터 구성하세요.

```
git push (코드 변경)
    │
    ▼
[GitHub Actions]  ← 직접 작성
    빌드 → ACR 푸시 → k8s/deployment.yaml 태그 업데이트 → 자동 커밋
    │
    ▼
[ArgoCD]  ← 직접 연결
    Git 변경 감지 → AKS 자동 배포
```

## 제공된 파일

| 파일 | 상태 |
|------|------|
| `Dockerfile` | ✅ 완성 |
| `k8s/*.yaml` | ✅ 완성 (placeholder 교체 필요) |
| `.github/workflows/` | ❌ 비어있음 — 직접 작성 |

## API 엔드포인트

| 엔드포인트 | 설명 |
|-----------|------|
| `GET /health` | 헬스체크 |
| `GET /api/notify/{order_id}` | 주문 알림 조회 |
| `GET /api/notify` | 전체 알림 목록 |

## 제출 방법

평가 가이드를 참고하세요: https://skilleat-labs.github.io/composable-ops-labs/evaluation/
