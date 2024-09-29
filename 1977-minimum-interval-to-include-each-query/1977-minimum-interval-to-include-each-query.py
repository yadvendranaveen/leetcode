class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted([(val, i) for i,val in enumerate(queries)])

        n = len(intervals)
        curr_idx, ans = 0, [-1]*len(queries)
        q = []

        for query, i in queries:
            while curr_idx<n and intervals[curr_idx][0] <= query:
                diff = intervals[curr_idx][1] - intervals[curr_idx][0] + 1
                heappush(q, (diff, intervals[curr_idx]))
                curr_idx += 1

            while q and q[0][1][1]<query:
                heappop(q)

            ans[i] = q[0][0] if q else -1

        return ans
            
        