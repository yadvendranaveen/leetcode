class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                mat[i][j] = -mat[i][j]
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                
        while q:
            i, j, d = q.popleft()

            for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and mat[ni][nj]==-1:
                    mat[ni][nj] = d+1
                    q.append((ni, nj, d+1))

                    
        return mat