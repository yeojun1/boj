# L=도로 길이
# N=가로등 갯수
# K=출력해야될 갯수
# A=가로등 위치
L,N,K=map(int,input().split())
A=list(map(int,input().split()))

# queue = [(좌표, 밝기), (좌표, 밝기)...]
# printedCoord = 이미 queue에 있는 좌표
# idx = queue에서 참조할 idx
import queue

queue = queue.Queue()
savedCoord = set()
ans = list()
idx = 0

for i in range(N):
    queue.put([A[i], 0])
    savedCoord.add(A[i])

while not queue.empty():
    # if len(savedCoord)>=K: break
    # if idx >= len(queue): idx=0
    q = queue.get()
    ans.append(q[1])

    if len(ans) >= K:
        break

    if not q[0]+1 in savedCoord and 0 <= q[0]+1 <= L:
        savedCoord.add(q[0]+1)
        queue.put([q[0]+1, q[1]+1])

    if not q[0]-1 in savedCoord and 0 <= q[0]-1 <= L:
        savedCoord.add(q[0]-1)
        queue.put([q[0]-1, q[1]+1])


    # if not queue[idx][0]+1 in savedCoord:
    #     queue.append([queue[idx][0]+1, queue[idx][1]+1])
    #     savedCoord.append(queue[idx][0]+1)
    # if not queue[idx][0]-1 in savedCoord:
    #     queue.append([queue[idx][0]-1, queue[idx][1]+1])
    #     savedCoord.append(queue[idx][0]-1)
    # idx+=1

for i in range(len(ans)):
    print(ans[i])

# for i in range(min(K, len(queue))):
#     print(queue[i][1])