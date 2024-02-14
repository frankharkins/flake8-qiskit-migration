import sys, subprocess

def cli():
    subprocess.run(["flake8", "--select", "QKT100"] + sys.argv[1:])
