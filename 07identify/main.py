import threading
import time


def threadFoo():
    #localに使う変数を定義できる
    i = threading.local()
    i=0
    while i<3:
        time.sleep(1)        
        i+=1

thread = threading.Thread(target=threadFoo,name="nameOfThread",daemon=True)
thread.start()

print(thread.ident)
print(thread.name)

thread.join()

print("---end---")
