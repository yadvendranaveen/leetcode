class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0

        def dfs(i,j):
            if not(0<=i<m and 0<=j<n): return
            if grid[i][j]=='1':
                grid[i][j]='0'
                dfs(i-1,j), dfs(i,j-1), dfs(i+1,j), dfs(i,j+1)        

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        return ans