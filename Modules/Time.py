import time

print("Seconds elapsed since the epoch are : ",time.time())
print("Time calculated acc. to given seconds is : ",time.gmtime())

ti = time.gmtime()
print("Time calculated using asctime() is : ",time.asctime(ti))
print("Time calculated using ctime() is : ",time.ctime())
time.sleep(4)
print("Stop execution : ",time.ctime())