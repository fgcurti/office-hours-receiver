import subprocess
import time
import requestfetcher
import os

def current_milli():
    return int(round(time.time() * 1000))

def get_pressed():
    return False

if __name__ == "__main__":
    rf = requestfetcher.RequestFetcher()

    print(rf.get_req())

    lastchecked_ms = 0
    req_str = ""
    process_handle = None

    print(current_milli)

    while True:
        if current_milli() >= lastchecked_ms + 1000:
            req_str = rf.get_req()
            # debug
            print("tick")
            lastchecked_ms = current_milli()
        if req_str != "":
            if process_handle == None:
                # placeholder
                process_handle = subprocess.Popen(["ls", "-a"])
        else:
            if process_handle != None:
                process_handle.kill()
                process_handle = None
        if get_pressed() == True:
            rf.clear_req()


