import threading
import time

lock = threading.Lock()
b = 0

def threadFoo(lock, addVal):
    global b
    with lock:
        localb = b
        time.sleep(3)
        localb += addVal
        b = localb
        print("val in thread: " + str(b))

thread1 = threading.Thread(target=threadFoo,args=(lock, 1,),daemon=True)
time.sleep(1)
thread2 = threading.Thread(target=threadFoo,args=(lock, 2,),daemon=True)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("final val: " + str(b))