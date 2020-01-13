class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        for count in range(k):
            d =[]
            for i in grid :
                e = []
                e.append(0)
                for j in range(len(i)):
                    if j == len(i)-1 :
                        e[0] = i[j]
                    else :
                        e.append(i[j])
                d.append(e)
            
            grid = d
            a = []
            for g in range(len(grid)) :
                a.append(grid[g][0])
            for g in range(len(grid)) :
                if g == len(a)-1 :
                    grid[0][0] = a[g]
                else :
                    grid[g+1][0] = a[g]
        
            
        return grid

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [0]*(min(501, arrLen))
        dp[0] = 1
        for s in range(steps):
            new_dp = []
            for i in range(len(dp)):
                new_dp.append(((0 if i == 0 else dp[i-1]) + dp[i] + (0 if i == len(dp)-1 else dp[i+1]))%(10**9+7))
            dp = new_dp
        return dp[0]