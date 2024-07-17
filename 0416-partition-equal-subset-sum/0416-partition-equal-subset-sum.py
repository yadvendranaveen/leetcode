class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(idx, rem):
            if rem==0: return True
            if idx<0: return False
            return dfs(idx-1, rem) or dfs(idx-1, rem-nums[idx])
        total = sum(nums)
        if total%2!=0: return False
        return dfs(len(nums)-1, total//2)
        