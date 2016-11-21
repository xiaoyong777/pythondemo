import  threading

i=0
def run_thread():
    global i # 使用全局变量必须使用global
    lock.acquire() # 加锁
    try:
        while(i<100):
            i=i+1
            print('thread %s ---%d' %( threading.current_thread().name,i))
    finally:
        lock.release() #释放

lock = threading.Lock()
t1 = threading.Thread(target=run_thread, args=())
t2 = threading.Thread(target=run_thread, args=())
t1.start()
t2.start()
t1.join() # join 使线程阻塞 用于线程同步
t2.join() # 在本程序中 线程执行完后才会执行下面的输出语句
print("thread ----------end---------"+str(i))