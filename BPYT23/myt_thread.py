import threading
import time
def sometask(task,delay,daemon=False):
    if daemon:
        count = 0
        while(True):
            count+=1
            print("hello",count)
    time.sleep(delay)
    print(task,"Taks is running\n")
t1 = threading.Thread(target=sometask,args=["myFirstTask",True,5],daemon=True)
t2 = threading.Thread(target=sometask,args=["mySecondTask",1])
t1.start()
t2.start()
print("started")
# t1.join()    # don't
# t2.join()
print("Joined")
print("end")