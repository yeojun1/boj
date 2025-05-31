import sys

N = int(sys.stdin.readline())
p = tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(N))
arrow = []

for i in range(N):
    tmp = N-1
    idx = p[i][0]
    for j in range(idx-1, -1, -1):
        # On 예제 입력 2
        # Traceback (most recent call last):
        #     File "C:\BOJ\15970.py", line 11, in <module>
        #         if p[j][1] == p[i][1]: tmp = min(abs(p[i][0]-p[tmp][0]), abs(p[i][0]-p[j][0])); continue
        #            ~^^^
        # IndexError: tuple index out of range
        if p[j][1] == p[i][1]: tmp = min(abs(p[i][0]-p[tmp][0]), abs(p[i][0]-p[j][0])); continue
    for j in range(idx+1, N):
        if p[j][1] == p[i][1]: tmp = min(abs(p[i][0]-p[tmp][0]), abs(p[i][0]-p[j][0])); continue
    arrow.append(tmp)    

print(arrow)
print(sum(arrow))