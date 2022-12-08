from functools import reduce

paper = 0
ribbon = 0

for e in open('INPUT').readlines():
  l, w, h = map(int, e.split('x'))
  sides = [l*w,w*h,h*l]
  paper += reduce(lambda x, y: x+y, map(lambda z:2*z, sides)) + min(sides)
  ribbon += min([l+w,w+h,h+l])*2+(l*w*h)

print(paper, ribbon)
