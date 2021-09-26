import platform
import subprocess

def clear_console():
    if platform.system() is "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)