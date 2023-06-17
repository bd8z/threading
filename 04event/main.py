import threading
import time

event = threading.Event()

def threadFoo():
    while True:
        print("thread start")
        time.sleep(0.2)
        #eventのフラグが立つまで待ち受ける（defalut:False）
        event.wait()
        print("thread end")

thread = threading.Thread(target=threadFoo,daemon=True)
thread.start()

ii = 0

print("-------------------defalut-----------------------")
while True:
    for i in range(5):
        time.sleep(0.3)
        print("main thread" + str(i))

    if ii%2 == 0:
        #set()によって待ち受け状態が解放される
        print("-------------------event.set()-----------------------")
        event.set()
    else:
        #clear()でフラグを落とす
        print("-------------------event.clear()-----------------------")

        event.clear()

    ii += 1
