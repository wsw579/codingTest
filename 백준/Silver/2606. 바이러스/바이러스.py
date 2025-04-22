from collections import deque

computer = int(input()) 
N =  int(input()) 
graph = [[] for _ in range(computer + 1)]

for _ in range(N):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)


def bfs(graph , start):
    visited =[False] * (computer + 1)
    q = deque([start])
    visited[start] = True
    count = 0 
    while q :
        v = q.popleft()
        for i in graph[v]:
            if not visited[i] :
                q.append(i)
                visited[i]=True
                count+=1
    return count 

print(bfs(graph,1))
		
