# ch0ik-v2: Gemini 기반 개인 AI 어시스턴트

C – Code is the language of logic and creation.  
H – Hack your way through problems with smart solutions.  
0 – 0s and 1s build the universe of software.  
I – If statements guide our decisions.  
K – Keep debugging, keep improving, keep going.

---

## 📋 소개

**ch0ik-upgrade**는 Google Gemini API를 활용한 개인용 AI 어시스턴트입니다. Streamlit 기반의 웹 인터페이스로 쉽고 빠르게 대화형 AI를 경험할 수 있습니다.

---

## 🚀 빠른 시작

### 1. Google Gemini API 키 발급

- [Google Cloud Console](https://console.cloud.google.com/)에서 프로젝트를 생성하고,
- [Gemini API 사용 설정](https://console.cloud.google.com/ai/generative-language/api) 후,
- [API 및 서비스 > 사용자 인증 정보](https://console.cloud.google.com/apis/credentials)에서 **API 키**를 발급받으세요.

### 2. .env 파일 생성

프로젝트 루트에 `.env` 파일을 만들고 아래와 같이 입력하세요:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. 필수 패키지 설치

가상환경을 권장합니다. 아래 명령어를 실행하세요:

```
pip install -r requirements.txt
```

### 4. 실행 방법

#### (1) 기본 실행

```
streamlit run app.py
```

#### (2) 배치 파일로 실행 (Windows)

- `run.bat` 또는 `run_with_venv.bat` 실행
- GUI 런처: `run_gui.bat` 실행

---

## 🛠️ 주요 기능

- **Gemini 최신 모델 지원**: 텍스트/비전 모델(`gemini 2.5 pro`)
- **대화 이력 관리**: 대화 초기화, 내보내기(JSON 저장)
- **창의성(temperature) 조절**
- **Streamlit 기반 직관적 UI**
- **.env 환경변수로 API 키 안전하게 관리**

---

## ❓ FAQ

### Q. "429 quota exceeded" 오류가 나와요!

- 무료 플랜은 분당/일일 요청 수가 매우 제한적입니다.
- 1~2분 후 재시도하거나, [유료 플랜](https://console.cloud.google.com/billing)으로 업그레이드하세요.

### Q. "404 model not found" 오류가 나와요!

- 모델 이름을 `gemini 2.5 pro` 등으로 정확히 입력해야 합니다.
- 사용 가능한 모델은 [공식 문서](https://ai.google.dev/gemini-api/docs/models) 참고.

### Q. OpenAI 키로는 안 되나요?

- 본 버전은 Google Gemini API만 지원합니다. `.env`에 반드시 `GEMINI_API_KEY`를 입력하세요.

---

## 📂 파일 구조

- `app.py` : 메인 Streamlit 앱
- `requirements.txt` : 필수 패키지 목록
- `run.bat`, `run_with_venv.bat` : 실행용 배치 파일(Windows)
- `.env` : Gemini API 키 저장 (직접 생성)

---

## 📝 참고

- [Gemini API 공식 문서](https://ai.google.dev/gemini-api/docs)
- [Streamlit 공식 문서](https://docs.streamlit.io/)

---

즐거운 AI 실험 되세요! 🚀
