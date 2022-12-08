import hashlib
from binascii import hexlify
import time
from multiprocessing import Pool

key = 'bgvyzdsv'
m5 = '00000'

def solve(i):
  key = 'bgvyzdsv'
  m5 = '00000'
  inc = i
  while True:
      m = hashlib.md5()
      m.update("{}{}".format(key, i).encode())
      if (m5 == m.hexdigest()[:5]):
        print(m.hexdigest(), key+str(i), "by "+str(inc))
        if ('0' == m.hexdigest()[5]):
          return True
      i += 4

class Worker():
    def __init__(self, workers):
      self.workers = workers
      self.pool = Pool(processes=workers)

    def callback(self, result):
      if result:
        print("Solution found! Yay!")
        self.pool.terminate()

    def do_job(self):
      for args in range(self.workers):
        self.pool.apply_async(solve, args=[args], callback=self.callback)
      self.pool.close()
      self.pool.join()
      print("good bye")


if __name__ == '__main__':
    start = time.time()
    w = Worker(4)
    w.do_job()
    print(time.time() - start)


