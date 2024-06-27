def BipartiteMatching(A : list[int], B : list[int]) -> int:
    def DFS(a : int) -> bool:
        if visited[a]:
            return False
        visited[a] = True
        for b in adj[a]:
            if B[b] == -1 or DFS(B[b]):
                A[a] = b
                B[b] = a
                return True
        return False
    N = len(A)
    M = len(B)
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if A[i] == B[j]:
                adj[i].append(j)
    A = [-1]*N
    B = [-1]*M
    ans = 0
    for i in range(N):
        visited = [False]*N
        if DFS(i):
            ans += 1
    return ans