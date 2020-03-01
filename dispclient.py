import subprocess
import time
import requestfetcher

def current_milli():
    return int(round(time.time() * 1000))

def get_pressed():
    return False

def runled(name_list):
    process_handle = None
    for i in range(0,len(name_list)):
        process_handle = subprocess.Popen(["sudo",\
        "../display16x32/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example",\
        "-f","../display16x32/rpi-rgb-led-matrix/fonts/6x10.bdf",\
        "--led-no-hardware-pulse", "-l", "1", "--led-rows=16",\
        "--led-cols=32", "-s", "2",name_list[i]])
        subprocess.check_call(["sudo", "kill",str(process_handle.pid)])
        time.sleep(7)

if __name__ == "__main__":
    rf = requestfetcher.RequestFetcher()

    lastchecked_ms = 0
    process_handle = None
    req_list_old = [-999]
    
    print(current_milli)

    while True:
        if current_milli() >= lastchecked_ms + 1000:
            req_list = rf.get_req()
            print("tick")
            lastchecked_ms = current_milli()
            if req_list != [] and req_list_old != req_list:
                req_list_old = req_list[:]
                runled(req_list)
            elif req_list == [] and req_list_old != req_list:
                req_list_old = req_list[:]
            elif req_list != [] and req_list_old == req_list:
                runled(req_list)
            if get_pressed() == True:
                #rf.clear_req()
                pass

