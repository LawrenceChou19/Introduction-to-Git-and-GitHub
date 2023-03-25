import difflib
import sys
file1 = open("cpu_usage.py").readlines()
file2 = open("cpu_usage_fixed.py").readlines()


delta = difflib.unified_diff(file1,file2)
sys.stdout.writelines(delta)