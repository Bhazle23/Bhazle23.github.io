class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:0, 1:1, 2:2}
        def climbStairsUtil(n):
            if n not in memo:
                memo[n] = climbStairsUtil(n-1) + climbStairsUtil(n-2)
            return memo[n]
        return climbStairsUtil(n)