class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def dfs(i):
            if i==len(s) : return True
            res = False
            curr = ""
            for j in range(i,len(s)+1):
                if curr in wordDict: res |= dfs(j)
                if j<len(s): curr += s[j]
            return res
        return dfs(0)      