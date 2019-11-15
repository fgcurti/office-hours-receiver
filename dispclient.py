import subprocess
import time
import requestfetcher
import os

rf = requestfetcher.RequestFetcher()

#####################
# TEMP WORKING STUFF#

print(rf.get_req())

os.system("echo -e \"\\a\"")

def get_pressed():
    return False

####################

lastchecked_ms = 0
req_str = ""
process_handle = None
current_milli = lambda: int(round(time.time() * 1000))

while True:
    if current_milli >= lastchecked_ms + 1000:
        req_str = rf.get_req()
        ### debug
        print("tick")
        lastchecked_ms = current_milli
    if req_str != "":
        if process_handle == None:
            process_handle = subprocess.Popen(["ls", "-a"])
    else:
        if process_handle != None:
            process_handle.kill()
            process_handle = None
    if get_pressed() == True:
        rf.clear_req()


