print(diff rearrange1.py rearrange2.py)
diff -u cpu_usage.py cpu_usage_fixed.py
#!/usr/bin/env python3

import psutil
def check_cpu_usage(percent):
    usage = psutil.cpu_percent()
    return usage < percent

if not check_cpu_usage(75):
    print("Error! CPU is overloaded")
else:
    print("Everything ok")
#create diff file
diff -u cpu_usage.py cpu_usage_fixed.py > cpu_usage.diff   
diff -u disk_usage.py disk_usage_fixed.py > disk_usage.diff 
#patch
patch cpu_usage.py < cpu_usage.diff
patch disk_usage.py < disk_usage.diff
cat disk_usage.diff