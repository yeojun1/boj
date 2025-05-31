import sys

def solve(time):
    h = time//60
    t = (time-h*60)//10
    o = time-h*60-t*10

    while o > 5: t+=1; o-=10
    while t > 3: h+=1; t-=6

    actions = [0]*5

    actions[0] = h

    if t > 0: actions[1]=t
    else: actions[2]=abs(t)

    if o > 0: actions[3]=o
    else: actions[4]=abs(o)

    while actions[2] > 0 and actions[3] == 5:
        actions[2] -= 1
        actions[3] = 0
        actions[4] += 5

    return actions

T = int(sys.stdin.readline())
result = []

for i in range(T):
    result.append(solve(int(sys.stdin.readline())))

for j in range(T): print(*result[j])
