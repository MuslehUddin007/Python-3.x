# syntax
# barrier = threading.Barrier(number_of_threads,action=none,timeout=Node)

import threading

barrier = threading.Barrier(3)

class thread(threading.Thread):
    def __init__(self,thread_ID):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
    def run(self):
        print(str(self.thread_ID) + "\n")
        print("Parties = " + str(barrier.parties) + "\n")
        print("n_waiting = " + str(barrier.n_waiting) + "\n")
        barrier.wait()

thread1 = thread(100)
thread2 = thread(101)

thread1.start()
thread2.start()
barrier.wait()
print("Exit\n")

print(str(barrier.broken) + "\n")
barrier.reset()
print("n_waiting after reset = " + str(barrier.n_waiting))
barrier.abort()
print("End")

# barrier.broken = A boolean that is True if the barrier is in the broken state
# barrier.parties = the number of threads required to pass the barrier
# barrier.abort = Put the barrier into a broken state
# barrier.reset = empty state
# barrier.wait(timeout = None) = 
# barrier.n_waiting = the number of threads currently waiting in the barrier
