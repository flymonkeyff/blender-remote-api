# 🛰️ Blender Remote API

Blender 렌더링 상태를 실시간으로 확인하고, 원격에서 렌더 시작/정지 명령을 내릴 수 있는 미니 API 서버입니다.  
무료로 배포 가능하고, iOS 앱에서도 접속 가능해요!

---

## 📦 기능 요약

| 기능         | 설명 |
|--------------|------|
| `/status` (GET) | 현재 프레임, 총 프레임, 렌더 진행 여부 확인 |
| `/status` (POST) | 블렌더에서 상태 전송 (예: frame, total 등) |
| `/command` (POST) | 원격에서 "start", "stop" 명령 전송 |
| `/poll` (GET) | 블렌더에서 명령 대기 (폴링) |

---

## 🌐 사용 예시

### 🔁 블렌더가 주기적으로 상태 전송

```bash
curl -X POST https://your-server.onrender.com/status \
-H "Content-Type: application/json" \
-d '{"frame": 123, "total": 240, "is_rendering": true}'
