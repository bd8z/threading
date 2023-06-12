import threading
import time


def nijou():
    while True:
        print("bool")
        time.sleep(1)

if __name__ == "__main__":

    #daemonをTrueにすると、メインスレッドの停止に応じて終了できる。
    thread = threading.Thread(target=nijou, name='thread1',daemon = True)

    thread.start()

    #threadの識別子を取得できる
    print(thread.ident)
    time.sleep(5)

    print("end")