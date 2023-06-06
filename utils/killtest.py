import sys
import os
import signal

def killit():
    a=os.getpid()
    print(a)
    os.kill(a,signal.CTRL_C_EVENT)
    
