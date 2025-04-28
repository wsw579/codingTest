from collections import deque

N = int(input())

graph = []

for _ in range(N) :
	graph.append(list(map(int, list(input().strip()))))

visited = [[False] * N for _ in range(N)]

result = [] 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    house_count = 1
    
    while(queue):
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    house_count += 1

        
    return house_count        
        
        
                                                  
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            house_count = bfs(i,j)
            result.append(house_count) 
            


result.sort()

print(len(result))

for count in result:
    print(count)


