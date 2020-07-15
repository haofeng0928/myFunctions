# threading.Thread的对象方法
# start()：创建线程后通过start启动线程，等待CPU调度，为run函数执行做准备；
# run()：线程开始执行的入口函数，函数体中会调用用户编写的target函数，或者执行被重载的run函数；
# join([timeout])：阻塞挂起调用该函数的线程，直到被调用线程执行完成或超时。通常会在主线程中调用该方法，等待其他线程执行完成。
# name、getName()&setName()：线程名称相关的操作；
# ident：整数类型的线程标识符，线程开始执行前（调用start之前）为None；
# isAlive()、is_alive()：start函数执行之后到run函数执行完之前都为True；
# daemon、isDaemon()&setDaemon()：守护线程相关；

import threading
import time


def start_test(arg):
    time.sleep(1)
    print('%s running...\n' % arg)


def join_test(arg):
    print("%s is running at: %s\n" % (arg, time.time()))
    time.sleep(1)
    print("%s is finished at: %s\n" % (arg, time.time()))


def daemon_test(arg):
    print("%s running at: %s" % (arg, time.time()))
    time.sleep(1)
    print("%s is finished at: %s" % (arg, time.time()))


if __name__ == '__main__':
    # 创建线程：实例化threading.Thread，传入初始化函数作为线程执行的入口
    t1 = threading.Thread(target=start_test, args=('Thread 1 is', ))
    t2 = threading.Thread(target=start_test, args=('Thread 2 is', ))
    t1.start()
    t2.start()
    print('start')

    # 在主线程中创建若干线程之后，线程之间没有任何协作和同步，除主线程之外每个线程都是从run开始被执行，直到执行完毕
    # 多线程执行：通过join方法让主线程阻塞，等待其创建的线程执行完成
    t_join = threading.Thread(target=join_test, args=('Thread join',))
    t_join.start()
    t_join.join()
    print("join at：%s" % time.time())

    # 将创建的线程指定为守护线程（daemon），则主线程执行完毕之后会立即结束未执行完的线程，然后结束程序
    t_daemon = threading.Thread(target=daemon_test, args=('Thread daemon',))
    t_daemon.setDaemon(True)
    t_daemon.start()
    print("daemon at：%s" % time.time())
