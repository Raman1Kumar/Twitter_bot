import threading
from startserver import serve
from make_poster_save_upload import making_poster_uploading
import sys
from killtest import killit

def check():
    print("worked after this")


# make a server to facilitate making of poster(To get poster from p5js it should be opened in browser on localhost:xxxx or 127.0.0.1 then selenium open that url in website to dowload it )
t1=threading.Thread(target=serve)

# Make poster -> Upload on Instagram
t2=threading.Thread(target=making_poster_uploading)

t1.start()
t2.start()

t2.join()



hello=t2.is_alive()

if hello==False:
    killit()


print("process terminated")
