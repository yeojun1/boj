N=int(input())
X=list(map(int,input().split()))
T=list(map(int,input().split()))
C=max(X)
minT=0

for _ in range(N-1):
    now=X.pop(len(X)-1)
    esta=max(C-now,T[len(T)-1]-(C-now))
    minT+=esta
    T=[T[t]-esta for t in range(len(T))]
    T.pop(len(T)-1)