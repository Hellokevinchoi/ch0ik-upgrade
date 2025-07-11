import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import threading
import os
import sys
import webbrowser
from datetime import datetime

class PersonalAILauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 개인 AI 어시스턴트 런처")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # 스타일 설정
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        self.process = None
        
    def setup_ui(self):
        # 메인 프레임
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 제목
        title_label = ttk.Label(main_frame, text="🤖 개인 AI 어시스턴트", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # 버튼 프레임
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # 기본 버전 버튼
        self.basic_btn = ttk.Button(button_frame, text="기본 버전 실행", 
                                   command=self.run_basic_version)
        self.basic_btn.grid(row=0, column=0, padx=(0, 10))
        
        # 고급 버전 버튼
        self.advanced_btn = ttk.Button(button_frame, text="고급 버전 실행", 
                                      command=self.run_advanced_version)
        self.advanced_btn.grid(row=0, column=1, padx=(10, 0))
        
        # 설정 프레임
        settings_frame = ttk.LabelFrame(main_frame, text="설정", padding="10")
        settings_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # 가상환경 생성 버튼
        self.create_venv_btn = ttk.Button(settings_frame, text="가상환경 생성", 
                                         command=self.create_venv)
        self.create_venv_btn.grid(row=0, column=0, padx=(0, 10))
        
        # 패키지 설치 버튼
        self.install_packages_btn = ttk.Button(settings_frame, text="패키지 설치", 
                                             command=self.install_packages)
        self.install_packages_btn.grid(row=0, column=1, padx=(10, 0))
        
        # 브라우저 열기 버튼
        self.open_browser_btn = ttk.Button(settings_frame, text="브라우저 열기", 
                                          command=self.open_browser)
        self.open_browser_btn.grid(row=0, column=2, padx=(10, 0))
        
        # 로그 프레임
        log_frame = ttk.LabelFrame(main_frame, text="실행 로그", padding="10")
        log_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # 로그 텍스트 영역
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, width=70)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 상태 프레임
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # 상태 라벨
        self.status_label = ttk.Label(status_frame, text="대기 중...")
        self.status_label.grid(row=0, column=0, sticky=tk.W)
        
        # 종료 버튼
        self.stop_btn = ttk.Button(status_frame, text="애플리케이션 종료", 
                                  command=self.stop_app, state='disabled')
        self.stop_btn.grid(row=0, column=1, sticky=tk.E)
        
        # 그리드 가중치 설정
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        status_frame.columnconfigure(0, weight=1)
        
        # 초기 로그
        self.log("🤖 개인 AI 어시스턴트 런처가 시작되었습니다.")
        self.log("가상환경과 패키지 설치 상태를 확인합니다...")
        
        # 상태 확인
        self.check_status()
        
    def log(self, message):
        """로그 메시지를 추가합니다."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, log_message)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def check_status(self):
        """가상환경과 패키지 상태를 확인합니다."""
        venv_exists = os.path.exists("personal-ai-env")
        env_exists = os.path.exists(".env")
        
        if venv_exists:
            self.log("✅ 가상환경이 존재합니다.")
        else:
            self.log("❌ 가상환경이 없습니다. '가상환경 생성' 버튼을 클릭하세요.")
            
        if env_exists:
            self.log("✅ .env 파일이 존재합니다.")
        else:
            self.log("❌ .env 파일이 없습니다. API 키를 설정해주세요.")
            
        self.log("준비 완료! 버튼을 클릭하여 애플리케이션을 실행하세요.")
        
    def create_venv(self):
        """가상환경을 생성합니다."""
        def create():
            self.log("가상환경을 생성하고 있습니다...")
            try:
                result = subprocess.run([sys.executable, "-m", "venv", "personal-ai-env"], 
                                      capture_output=True, text=True, check=True)
                self.log("✅ 가상환경이 성공적으로 생성되었습니다.")
                self.install_packages()
            except subprocess.CalledProcessError as e:
                self.log(f"❌ 가상환경 생성 실패: {e.stderr}")
                messagebox.showerror("오류", "가상환경 생성에 실패했습니다.")
                
        threading.Thread(target=create, daemon=True).start()
        
    def install_packages(self):
        """필요한 패키지를 설치합니다."""
        def install():
            self.log("패키지를 설치하고 있습니다...")
            try:
                # 가상환경의 pip 경로
                if os.name == 'nt':  # Windows
                    pip_path = "personal-ai-env\\Scripts\\pip"
                else:  # Unix/Linux
                    pip_path = "personal-ai-env/bin/pip"
                    
                packages = ["google-generativeai", "streamlit", "python-dotenv", "requests", "Pillow"]
                
                for package in packages:
                    self.log(f"설치 중: {package}")
                    result = subprocess.run([pip_path, "install", package], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        self.log(f"✅ {package} 설치 완료")
                    else:
                        self.log(f"❌ {package} 설치 실패: {result.stderr}")
                        
                self.log("✅ 패키지 설치가 완료되었습니다.")
                
            except Exception as e:
                self.log(f"❌ 패키지 설치 중 오류: {str(e)}")
                messagebox.showerror("오류", "패키지 설치에 실패했습니다.")
                
        threading.Thread(target=install, daemon=True).start()
        
    def run_basic_version(self):
        """기본 버전을 실행합니다."""
        self.run_app("app.py", "기본 버전")
        
    def run_advanced_version(self):
        """고급 버전을 실행합니다."""
        self.run_app("advanced_app.py", "고급 버전")
        
    def run_app(self, app_file, version_name):
        """애플리케이션을 실행합니다."""
        if self.process:
            messagebox.showwarning("경고", "이미 실행 중인 애플리케이션이 있습니다.")
            return
            
        def run():
            self.log(f"{version_name}을 실행하고 있습니다...")
            
            # 가상환경의 Python 경로
            if os.name == 'nt':  # Windows
                python_path = "personal-ai-env\\Scripts\\python"
            else:  # Unix/Linux
                python_path = "personal-ai-env/bin/python"
                
            try:
                self.process = subprocess.Popen([python_path, "-m", "streamlit", "run", app_file],
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                              text=True)
                
                self.log(f"✅ {version_name}이 시작되었습니다.")
                self.log("브라우저에서 http://localhost:8501 로 접속하세요.")
                
                # UI 업데이트
                self.root.after(0, self.update_ui_running)
                
                # 프로세스 모니터링
                stdout, stderr = self.process.communicate()
                
                if self.process.returncode == 0:
                    self.log(f"✅ {version_name}이 정상적으로 종료되었습니다.")
                else:
                    self.log(f"❌ {version_name} 실행 중 오류: {stderr}")
                    
            except Exception as e:
                self.log(f"❌ {version_name} 실행 실패: {str(e)}")
                messagebox.showerror("오류", f"{version_name} 실행에 실패했습니다.")
            finally:
                self.process = None
                self.root.after(0, self.update_ui_stopped)
                
        threading.Thread(target=run, daemon=True).start()
        
    def update_ui_running(self):
        """실행 중일 때 UI를 업데이트합니다."""
        self.status_label.config(text="실행 중...")
        self.basic_btn.config(state='disabled')
        self.advanced_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        
    def update_ui_stopped(self):
        """중지되었을 때 UI를 업데이트합니다."""
        self.status_label.config(text="대기 중...")
        self.basic_btn.config(state='normal')
        self.advanced_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        
    def stop_app(self):
        """실행 중인 애플리케이션을 종료합니다."""
        if self.process:
            self.log("애플리케이션을 종료하고 있습니다...")
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
                self.log("✅ 애플리케이션이 종료되었습니다.")
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.log("⚠️ 애플리케이션을 강제 종료했습니다.")
            self.process = None
            self.update_ui_stopped()
        else:
            messagebox.showinfo("정보", "실행 중인 애플리케이션이 없습니다.")
            
    def open_browser(self):
        """브라우저에서 애플리케이션을 엽니다."""
        try:
            webbrowser.open("http://localhost:8501")
            self.log("브라우저를 열었습니다.")
        except Exception as e:
            self.log(f"브라우저 열기 실패: {str(e)}")
            messagebox.showerror("오류", "브라우저를 열 수 없습니다.")

def main():
    root = tk.Tk()
    app = PersonalAILauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main() 