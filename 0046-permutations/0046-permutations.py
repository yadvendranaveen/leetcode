class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n, ans = len(nums), []

        curr, inCurr = [], [False]*n
        def dfs():
            if len(curr)==n:    
                ans.append(curr[:])
                return
            for i,num in enumerate(nums):
                if not inCurr[i]:
                    curr.append(num)
                    inCurr[i] = True
                    dfs()
                    curr.pop()
                    inCurr[i] = False
        dfs()
        return ans
        