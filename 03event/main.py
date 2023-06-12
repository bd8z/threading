import threading
import time

#今回の場合はmainスレッドからthreadの実行をeventを使ってブロックできる
event = threading.Event()

def race():
    while True:
        print("thread start")
        time.sleep(0.1)
        #特定のインスタンス化されたeventのフラグが立つまで待ち受ける（defalut:False）
        event.wait()
        print("thread end")

thread = threading.Thread(target=race,daemon=True)
thread.start()

ii = 0
while True:
    for i in range(5):
        time.sleep(0.3)
        print("main thread" + str(i))

    if ii%2 == 1:
        #set()によって待ち受け状態が解放される
        print("-------------------event.set()-----------------------")
        event.set()
    else:
        #clear()でフラグを落とす
        print("-------------------event.clear()-----------------------")

        event.clear()

    ii += 1


