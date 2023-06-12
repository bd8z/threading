import threading
import time

#今回の場合はmainスレッドからthreadの実行をeventを使ってブロックできる
event = threading.Event()

def race():
    while True:
        print("thread start")
        time.sleep(0.1)
        #timeoutを使うことでデッドロックを解放できる
        #用途 mainスレッド側での処理の時間が読めなくて、こっちのスレッドで何か負荷をかけ続けている状況の時、解放させるとかか
        event.wait(timeout=5)
        print("thread end")

thread = threading.Thread(target=race,daemon=True)
thread.start()

while True:
    for i in range(10):
        time.sleep(0.3)
        print("main thread" + str(i))

