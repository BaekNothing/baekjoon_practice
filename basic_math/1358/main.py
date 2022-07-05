import math

w, h, x, y, p = input().split()
w = int(w)
h = int(h)
x = int(x)
y = int(y)
p = int(p)

def isIn(pos, x, y, range) -> bool :
    return math.dist([pos[0], pos[1]], [x, y]) <= range

result = 0
for i in range(p) : 
    xPos, yPos = input().split()
    xPos = int(xPos)
    yPos = int(yPos)
    pos = [int(xPos), int(yPos)]
    if x <= xPos and xPos <= x + w and y <= yPos and yPos <= y + h :
        result += 1
    elif isIn(pos, x, (y + h / 2), (h / 2)) :
        result += 1
    elif isIn(pos, x + w, y + h / 2, h / 2) : 
        result += 1

print(result)