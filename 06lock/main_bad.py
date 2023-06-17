import threading
import time

b = 0

def threadFoo(addVal):
    global b
    localb = b
    time.sleep(3)
    localb += addVal
    b = localb
    print("val in thread: " + str(b))

thread1 = threading.Thread(target=threadFoo,args=(1,),daemon=True)
time.sleep(1)
thread2 = threading.Thread(target=threadFoo,args=(2,),daemon=True)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("final val: " + str(b))