import threading
import time

event = threading.Event()

def threadFoo():
    while True:
        print("thread start")
        time.sleep(0.1)
        #timeoutを使うことでデッドロックを解放できる
        event.wait(timeout=3)
        print("thread end")

thread = threading.Thread(target=threadFoo,daemon=True)
thread.start()

while True:
    for i in range(5):
        time.sleep(0.3)
        print("main thread" + str(i))