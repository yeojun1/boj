import sys

def solve(time):
    h = time//60
    t = (time-h*60)//10
    o = time-h*60-t*10

    if t > 3:
        t -= 6
        h += 1
    
    if o > 5:
        o -= 10
        t += 1
    
    if t < o and o == 5:
        t += 1
        o -= 10
    
    actions = [0]*5

    # h는 무조건 양수 또는 0이므로 그냥 더하기
    actions[0] += h
    
    if t >= 0:
        actions[1] += t
    else:
        actions[2] += abs(t)
    
    if o >= 0:
        actions[3] += o
    else:
        actions[4] += abs(o)
    
    return actions



T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(*solve(N))