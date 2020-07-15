import multiprocessing
import os


def process_test(name):
    print("Process name: %s, pid: %s " % (name, os.getpid()))


if __name__ == "__main__":
    # 创建进程：实例化multiprocessing.Process，并传入初始化函数对象作为进程执行入口
    proc = multiprocessing.Process(target=process_test, args=('proc',))
    proc.start()
    proc.join()
    print("process pid: %s" % proc.pid)
    print("current process pid: %s" % os.getpid())

    # 另一种创建进程的方式：subprocess模块可以在程序执行过程中调用外部的程序
    import subprocess
    subprocess.Popen(['notepad'])
