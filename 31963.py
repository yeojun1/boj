from math import log2,ceil
N = int(input())
A = list(map(int, input().split()))
res=[0]

for i in range(1,N):
    res.append(max(0,int(ceil(log2(A[i-1]/A[i])))+res[i-1]))

print(sum(res))