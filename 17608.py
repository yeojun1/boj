from sys import stdin

h = []
for _ in range(int(stdin.readline())): h.append(int(stdin.readline()))
h.reverse()

ans, maxH = 0, 0

for i in range(len(h)):
    if h[i] > maxH:
        ans+=1
        maxH=h[i]

print(ans)