import subprocess
import sys
import time

def start_web_app():
    print("Starting the web server...")
    try:
        # Launch the server.py script as a subprocess
        subprocess.run([sys.executable, "server.py"])
    except Exception as e:
        print(f"Failed to start server: {e}")

if __name__ == '__main__':
    start_web_app()
