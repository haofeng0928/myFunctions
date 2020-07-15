# 多线程 & 多进程
import threading
import multiprocessing
import time


def test(arg):
    var = 0
    for i in range(100000000):
        var += 1


if __name__ == '__main__':
    # 开启两个线程分别做一亿次加一操作，和单独使用一个线程做一亿次加一操作
    t1 = threading.Thread(target=test, args=('This is thread 1',))
    t2 = threading.Thread(target=test, args=('This is thread 2',))
    start_time = time.time()
    # 并行
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # 串行
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    print("Two thread cost time: %s" % (time.time() - start_time))
    start_time = time.time()
    test("This is thread 0")
    print("One thread cost time: %s" % (time.time() - start_time))

    # 使用两个进程进行上面的操作
    p1 = multiprocessing.Process(target=test, args=("proc 1",))
    p2 = multiprocessing.Process(target=test, args=("proc 2",))
    start_time = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Two process cost time: %s" % (time.time() - start_time))
    start_time = time.time()
    test("proc 0")
    print("One process cost time: %s" % (time.time() - start_time))
