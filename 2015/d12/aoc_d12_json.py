import json

objs = json.loads(open('input','rt').read())


def recurse(o):
    p1 = 0
    if type(o) == type({}):
        if 'red' in o.values():
            return 0
        for k,v in o.items():
            p1 += recurse(v)
    elif type(o) == type([]):
        for i in o:
          p1 += recurse(i)
    else:
       try:
         v = int(o)
         return int(o)
       except:
         return 0
    return p1
print(recurse(objs))
