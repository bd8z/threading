import threading
import time


def threadFoo():
    while True:
        print("foo")
        time.sleep(1)

if __name__ == "__main__":

    #daemonをTrueにすると、メインスレッドと同時に終了できる
    thread = threading.Thread(target=threadFoo, name='thread1',daemon = True)
    thread.start()
    time.sleep(5)
    print("---end---")