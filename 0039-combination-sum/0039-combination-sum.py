class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n, ans = len(candidates), []

        comb = []
        def dfs(rem, start):
            if rem<0: return 
            if not rem: 
                ans.append(list(comb))
                return
            for i in range(start, n):
                comb.append(candidates[i])
                dfs(rem-candidates[i], i)
                comb.pop()
        dfs(target, 0)
        return ans

        