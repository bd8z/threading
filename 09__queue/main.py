import queue
import threading
import time

queue = queue.Queue() # newthread -> main

def threadFoo(q):
    i = 0
    while True:
        time.sleep(1)
        q.put(i)
        print("thread put:" + str(i))
        i+=1

if __name__ == "__main__":
    thread = threading.Thread(target=threadFoo, args=(queue,),daemon = True)
    thread.start()

    while True:
        try:
            print("main get:"+str(queue.get(timeout=3)))
        except :
            print("error")