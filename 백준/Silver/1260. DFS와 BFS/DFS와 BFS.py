from collections import deque

N, M , V = map(int, input().split())

graph = [[] for _ in range(N+1) ]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,N+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ") 
    for current in graph[v]:
        if not visited[current]:
            dfs(graph,current,visited)
	

def bfs(graph,start):
    visited = [False]*(N+1)
    q = deque([start])
    visited[start] = True
    
    while q:
        v=q.popleft()
        print(v,end=" ")
        for current in graph[v]:
            if not visited[current]:
                q.append(current)
                visited[current]=True


visited_dfs = [False] * (N + 1) 
dfs(graph, V, visited_dfs)
print()
bfs(graph,V)