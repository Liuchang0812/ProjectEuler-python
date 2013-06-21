import threading , time , random
count = 0
from threading import Thread

class Counter(Thread):
    def __init__(self , lock , threadName):
        super(Counter , self).__init__(name = threadName)
        self.lock = lock
    def run(self):

        global count
        self.lock.acquire()
        for i in xrange(1000):
            count = count + 1
        self.lock.release()
lock = threading.Lock()

for i in range(5):
    Counter(lock , "thread-"+str(i)).start()
time.sleep(2)

print count