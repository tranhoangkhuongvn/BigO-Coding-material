#Review DFS implementation
MAX = 100
V = None
E = None
visited = [False] * MAX
path = [0]*MAX
graph = [[] for i in range(MAX)]

def DFS(src):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    s = []
    visited[src] = True
    s.append(src)
    
    while len(s) > 0:
        src = s[-1]
        s.pop()
        for v in graph[src]:
            if visited[v] == False:
                visited[v] = True
                s.append(v)
                path[v] = src

def printPath(s,f,path):
    b = []
    if f == s:
        print(f)
        return
    if path[f] == -1:
        print('No path')
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    for i in range(len(b)-1,-1,-1):
        print(b[i], end = ' ')
        

if __name__ == '__main__':
    V, E = map(int,input().split())
    for i in range(E):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 0
    d = 5
    DFS(s)
    printPath(s,d,path)
