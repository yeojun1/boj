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

# def min_collection_time(N, X, T):
#     houses = sorted(zip(X, T))
    
#     current_time = 0
#     current_pos = 0
    
#     for x, t in houses:
#         travel_time = abs(x - current_pos)
#         current_time += travel_time
#         current_pos = x
#         if current_time < t:
#             current_time = t  # 기다림
    
#     # 마지막 집에서 회사로 돌아가기
#     current_time += current_pos  # 현재 위치에서 0까지
    
#     return current_time


# print(minT)

# 0. 가는시간 구하기: 만약 가야하는곳보다 현위치가 작다면 가야하는곳-현위치 / 아니면 현위치-가야하는곳
# 1. 만약 가는 시간이 기다리는 시간보다 크다면 가는시간 / 기다리는 시간이 크면 기다리는 시간-가는시간
# 2. 1번 걸린시간에 더하기
# 3. 현위치 1번에서 이동한 곳으로 바꾸기