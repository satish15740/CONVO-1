import os

def restart_system():
    try:
        os.system("sudo reboot")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    restart_system()
