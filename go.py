# Attempt to bootstrap
import os
import subprocess
import sys

def main():
    prefix = os.path.abspath(os.path.dirname(__file__))
    virtualenv = os.path.join(prefix, "gamecraft-it-py")
    python = os.path.join(virtualenv, "bin", "python")
    if not os.path.isfile(python):
        print("Attempting to bootstrap, hold on to your pants!")
        subprocess.check_call(["virtualenv", virtualenv])
        pip = os.path.join(virtualenv, "bin", "pip")
        requirements = os.path.join(prefix, "requirements.txt")
        subprocess.check_call([pip, "install", "-r", requirements])
        subprocess.check_call([pip, "install", "-e", prefix])

    subprocess.call([python, "-m", "gamecraft.main"] + sys.argv[1:])

if __name__ == '__main__':
    main()
