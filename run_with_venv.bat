@echo off
echo 🤖 가상환경에서 개인 AI 어시스턴트를 시작합니다...
echo.

REM 가상환경이 존재하는지 확인
if not exist "personal-ai-env" (
    echo 가상환경을 생성합니다...
    python -m venv personal-ai-env
    if errorlevel 1 (
        echo ❌ 가상환경 생성에 실패했습니다.
        echo Python이 올바르게 설치되어 있는지 확인해주세요.
        pause
        exit /b 1
    )
    echo ✅ 가상환경이 생성되었습니다.
)

REM 가상환경 활성화
echo 가상환경을 활성화합니다...
call personal-ai-env\Scripts\activate
if errorlevel 1 (
    echo ❌ 가상환경 활성화에 실패했습니다.
    pause
    exit /b 1
)

REM pip 업그레이드
echo pip를 업그레이드합니다...
python -m pip install --upgrade pip

REM 패키지 설치
echo.
echo 1. 필요한 패키지를 설치합니다...
pip install openai streamlit python-dotenv requests Pillow
if errorlevel 1 (
    echo ❌ 패키지 설치에 실패했습니다.
    echo 인터넷 연결을 확인하고 다시 시도해주세요.
    pause
    exit /b 1
)

REM .env 파일 확인
if not exist ".env" (
    echo.
    echo ⚠️  .env 파일이 없습니다.
    echo OpenAI API 키를 설정해주세요.
    echo.
    echo 예시:
    echo OPENAI_API_KEY=your_actual_api_key_here
    echo.
    pause
)

REM 애플리케이션 실행
echo.
echo 2. 애플리케이션을 실행합니다...
echo 브라우저에서 http://localhost:8501 로 접속하세요
echo 종료하려면 Ctrl+C를 누르세요
echo.
streamlit run app.py

pause 