import time, sys, queue
from multiprocessing.managers import BaseManager
import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]


class QueueManager(BaseManager):
    pass
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('正在连接主服务%s......' % server_addr)
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

while True:
    try:
        n = task.get(timeout=1)
        print('从Queue取到了数字 %d' % n)
        print('正在执行运算 %d * %d' % (n, n))
        r = '%d * %d = %d  (from %s @ %s)' % (n, n, n * n, os.getpid(), ip)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('任务队列已空')
        break

print('工作进程【%s】已结束' % os.getpid())