import queue
import threading
import time

queue01 = queue.Queue()

def nijou(q):
    i = threading.local
    i = 0
    while True:
        print("send")
        time.sleep(1)
        q.put(i)
        i+=1

if __name__ == "__main__":

    #daemonをTrueにすると、メインスレッドの停止に応じて終了できる。
    thread = threading.Thread(target=nijou, name='thread1', args=(queue01,),daemon = True)

    thread.start()

    #threadの識別子を取得できる

    for i in range(100):
        time.sleep(0.1)
        if queue01.empty():
            pass
        else:
            print("get!")
            print(queue01.get())
            print(queue01.qsize())

    print("end")