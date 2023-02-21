import threading
import time

def task(arg):
    time.sleep(2)
    print('hello')

t = threading.Thread(target=task, args=(1,))
t.setDaemon(False) # 设置为守护线程
t.start()

print('world')