class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n, ans = len(nums), []

        curr = []
        def dfs():
            if len(curr)==n:    
                ans.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs()
                    curr.pop()
        dfs()
        return ans
        