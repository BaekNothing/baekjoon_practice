import subprocess
import sys
import pip

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def pip_install_requirements(requirements_dir):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_dir.rstrip(".txt")+".txt"])

try :
    pip_install_requirements('./requirements.txt')
except :
    print("error")