#!/usr/bin/env python3
import shutil
import sys

def check_reboot():
    """Returns True if the computer has a pending rebooot."""
    return os.path.exists('/run/reboot-required')

def check_disk_usage(disk, min_gb, min_percent):
    """Returns True if there is enough free dish space, false otherwise"""
    du=shutil.disk_usage(disk)
    #calculate the percentage of free space
    percent_free=du.free/du.total*100
    #Calculate how many free gigabytes
    gigabytes_free = du.free/ 2**30

    if percent_free < min_percent or gigabytes_free < min_gb:
       return False
    return True


if not check_disk_usage("/", 2, 10):  # No '/',2*2**30,10
    print("ERROR:Not enough disk space")
    sys.exit(1)                    #return 1 didn't come there because it will c>

else:
    print("Everything is OK")
    sys.exit(0)                    #return 0

def main():
    if check_reboot():
       print("Pending Rebooot.")
    if check_disk_usage("/", 2, 10)
       print("Disk full.")
       sys.exit(1)
    
    print("Everything Ok.")
    sys.exit(0)

 main()   

