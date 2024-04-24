
from multiprocessing import Pool,Queue
import os
import psutil

# 定义一个队列用于存储进程id
# queue = Queue()

# 用于计算平方和将运行函数的进程id写入队列
def f(x):
    # queue.put(os.getpid())
    return x * x

if __name__ == '__main__':
    # 逻辑cpu个数
    count = psutil.cpu_count()
    print(f'My Computer CPU Number is {count}')

    with Pool(count * 2) as p:
        # 并行计算
        res = p.map(f, range(1, 101))
        print(f'计算平方的结果是:{res}')

    # 并行计算用到的进程id
    # pids = set()
    # while not queue.empty():
    #     pids.add(queue.get())
    
    # print(f'用到的进程id是: { pids }')
    # pids.clear()
    # queue.close()
    