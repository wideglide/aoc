import hashlib
from binascii import hexlify
import time

key = 'bgvyzdsv'
m5 = '00000'
i = 0

start = time.time()
while True:
    m = hashlib.md5()
    m.update("{}{}".format(key, i).encode())
    if (m5 == m.hexdigest()[:5]):
      print(m.hexdigest(), key+str(i))
      if ('0' == m.hexdigest()[5]):
        print(m.hexdigest(), key+str(i))
        break
    i += 1
print(time.time()-start)


