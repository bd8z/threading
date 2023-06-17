import queue
import threading
import time

queue01 = queue.Queue() # main-> newthread
queue02 = queue.Queue() # newThread -> main

def threadFoo(q1,q2):
    time.sleep(1)
    localVal = threading.local()
    while True:
        if q1.empty():
            time.sleep(0.2)
            print("thread waiting..")
        else:
            localVal = q1.get()
            print("thread q1.get():"+str(localVal))
            
            sendVal = localVal+100
            print("thread q1.put():"+str(sendVal))
            q2.put(sendVal)


if __name__ == "__main__":
    thread = threading.Thread(target=threadFoo, args=(queue01,queue02,),daemon = True)
    thread.start()

    i=0
    while True:
        print("main q1.put():"+str(i))
        queue01.put(i)

        time.sleep(1)
        if queue02.empty():
            pass
        else:
            val = queue02.get()
            print("thread q2.get():"+str(val))
            print("------------")

        i+=1