import threading
import time


def nijou():
    for i in range(5):
        print("nijou" + str(i))
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=nijou, name='thread1')

    thread.start()

    #threadの処理が終了するまでmainスレッドの処理をブロックできる。同期的な処理が書ける。
    thread.join()

    print("---end---")



    thread = threading.Thread(target=nijou, name='thread1')

    thread.start()

    #タイムアウトもできるが、スレッドが止まるわけではない。
    #メインスレッドのデッドロックを回避できる。
    thread.join(timeout=2)

    print("---end---")


    time.sleep(5)


    #joinのtimeoutとdemonを併用することでメインスレッドの終了に応じてスレッドを落とせる。
    #いきなり落ちるのトランザクションをロックしてしまったりで推奨されない。
    #べスプラはEventを使う
    thread = threading.Thread(target=nijou, name='thread1',daemon=True)

    thread.start()

    thread.join(timeout=2)

    print("---end---")
