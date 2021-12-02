#!/usr/bin/env python

import os
import sys
import shutil

if len(sys.argv) != 2:
    print(f"Usage: ./{sys.argv[0]} + $DAY_NUM")

if os.path.exists(sys.argv[1] + ".1"):
    print("Day already exists")

dir_1 = "./" + sys.argv[1] + ".1"
dir_2 = "./" + sys.argv[1] + ".2"

os.mkdir(dir_1)
os.mkdir(dir_2)
shutil.copyfile("./template.py", dir_1 + "/solve.py")
shutil.copyfile("./template.py", dir_2 + "/solve.py")
os.chmod(dir_1 + "/solve.py", 0o700)
os.chmod(dir_2 + "/solve.py", 0o700)
