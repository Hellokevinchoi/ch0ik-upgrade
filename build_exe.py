#!/usr/bin/env python3
"""
개인 AI 어시스턴트 런처를 실행 파일로 빌드하는 스크립트
"""

import os
import subprocess
import sys

def install_pyinstaller():
    """PyInstaller를 설치합니다."""
    print("PyInstaller를 설치하고 있습니다...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        print("✅ PyInstaller 설치 완료")
        return True
    except subprocess.CalledProcessError:
        print("❌ PyInstaller 설치 실패")
        return False

def build_exe():
    """실행 파일을 빌드합니다."""
    print("실행 파일을 빌드하고 있습니다...")
    
    # PyInstaller 명령어
    cmd = [
        "pyinstaller",
        "--onefile",  # 단일 실행 파일
        "--windowed",  # 콘솔 창 숨김
        "--name=PersonalAI_Launcher",  # 실행 파일 이름
        "--icon=icon.ico",  # 아이콘 (있는 경우)
        "--add-data=app.py;.",  # app.py 포함
        "--add-data=advanced_app.py;.",  # advanced_app.py 포함
        "--add-data=.env;.",  # .env 파일 포함
        "app_launcher.py"
    ]
    
    try:
        # 아이콘이 없으면 아이콘 옵션 제거
        if not os.path.exists("icon.ico"):
            cmd = [arg for arg in cmd if not arg.startswith("--icon")]
        
        # .env 파일이 없으면 제거
        if not os.path.exists(".env"):
            cmd = [arg for arg in cmd if not arg.startswith("--add-data=.env")]
        
        result = subprocess.run(cmd, check=True)
        print("✅ 실행 파일 빌드 완료!")
        print("📁 dist 폴더에 PersonalAI_Launcher.exe 파일이 생성되었습니다.")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 빌드 실패: {e}")
        return False

def main():
    print("🤖 개인 AI 어시스턴트 런처 빌더")
    print("=" * 50)
    
    # PyInstaller 설치 확인
    try:
        import PyInstaller
        print("✅ PyInstaller가 이미 설치되어 있습니다.")
    except ImportError:
        print("PyInstaller가 설치되어 있지 않습니다.")
        if not install_pyinstaller():
            return
    
    # 빌드 실행
    if build_exe():
        print("\n🎉 빌드가 완료되었습니다!")
        print("📂 dist/PersonalAI_Launcher.exe 파일을 실행하세요.")
        print("\n💡 사용 방법:")
        print("1. PersonalAI_Launcher.exe를 더블클릭")
        print("2. '가상환경 생성' 버튼 클릭")
        print("3. '패키지 설치' 버튼 클릭")
        print("4. '기본 버전 실행' 또는 '고급 버전 실행' 버튼 클릭")
    else:
        print("\n❌ 빌드에 실패했습니다.")
        print("오류 메시지를 확인하고 다시 시도해주세요.")

if __name__ == "__main__":
    main() 