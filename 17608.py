h = []
for _ in range(int(input())): h.insert(0, int(input()))
h = list(dict.fromkeys(h))
N = len(h)

ans = 0
maxH = 0
# i = 0

# while i <= N-1:
#     ans += 1
#     maxH = h[i]
#     # 현재 인덱스보다 뒤에 있는 원소 중 더 큰 원소 찾기
#     while i <= N-1 and h[i] <= maxH: i += 1

for i in range(N):
    if h[i] > maxH:
        ans+=1
        maxH=h[i]

print(ans)
