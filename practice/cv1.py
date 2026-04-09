import math
def triangle(x: float,y: float)->float:
    c = math.sqrt(x**2+y**2)
    return c

def cva():
    data = 3,7,6,11,5,5,8,9
    prev = 0

    for value in data:
        if value-prev == 0:
            print("deleni nulou nejde")
        else:
            print(value/(value - prev))
        prev = value

def cvb():
    scores = [50, 80, 45, 90, 30, 60]
    for i in range(0,len(scores)-1,-1):
        if scores[i] < 50:
            scores.remove(i)
    print(scores)
cvb()
