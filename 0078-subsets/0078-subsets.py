class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(idx, curr):
            if idx<0: 
                ans.append(curr[:])
                return
            # case 1: when element at idx is not chosen
            dfs(idx-1, curr) 

            #case 2: when element at idx is chosen
            curr.append(nums[idx])
            dfs(idx-1, curr)
            curr.pop()
            
        dfs(len(nums)-1, [])
        return ans