import threading
from start_server import serve
from start_making_poster import first
import sys
from killtest import killit

def check():
    print("worked after this")


t1=threading.Thread(target=serve)
t2=threading.Thread(target=first)

t1.start()
t2.start()

t2.join()



hello=t2.is_alive()

if hello==False:
    killit()


print("came here")
