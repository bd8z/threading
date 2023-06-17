import threading
import time


def threadFoo():
    for i in range(5):
        print("foo" + str(i))
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=threadFoo, name='thread1',daemon=True)
    thread.start()

    thread.join(timeout=2)
    print("---end---")

    time.sleep(5)   