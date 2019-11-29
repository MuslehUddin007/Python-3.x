# syntax
# threading.Timer(interval,function,args = None,kwargs = None)

import threading

def gfg():
    print("Md Musleh Uddin Khan")

timer = threading.Timer(2.0,gfg)
timer.start()
print("Exit\n")

# Cancelling a timer
def gg():
    print("Md Musahid Uddin")

timer = threading.Timer(5.0,gg)
timer.start()
print("Cancelling timer\n")
timer.cancel()
print("Exit\n")