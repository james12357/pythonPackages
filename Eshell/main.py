import os
import sys


def sp(s: str):
    t = s.split(" ")
    cmd = t[0]
    args = t[1:]
    return {"cmd": cmd, "args": args}


sys.path.append("lib")
while True:
    cwd = os.getcwd()
    c = sp(input(f"{cwd}@localhost#"))
    exec(f"import {c['cmd']}")
    exec(f"{c['cmd']}.main({','.join(c['args'])})")
