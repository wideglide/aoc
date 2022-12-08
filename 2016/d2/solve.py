

f = [l.strip() for l in open('input').readlines() ] 

keypad = [\
[1,2,3],\
[4,5,6],\
[7,8,9]]
x = 1
y = 1
code = ""

for moves in f:
    for move in moves:
        if move == "U": y = max((y-1),0) 
        if move == "D": y = min((y+1),2)
        if move == "R": x = min((x+1),2)
        if move == "L": x = max((x-1),0)
    code += str(keypad[y][x])
print code

keypad2 = [ \
['0','0','1','0','0'], \
['0','2','3','4','0'], \
['5','6','7','8','9'], \
['0','A','B','C','0'], \
['0','0','D','0','0']]
code = ""
x = 0
y = 2
for moves in f:
    for move in moves:
        tx = x
        ty = y
        if move == "U": ty = max((y-1),0) 
        if move == "D": ty = min((y+1),4)
        if move == "R": tx = min((x+1),4)
        if move == "L": tx = max((x-1),0)
        if keypad2[ty][tx] != '0':  
            x = tx
            y = ty
    code += keypad2[y][x]
print code
