class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # dp[i][j] represents if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns that can match an empty string (e.g., "a*", "a*b*")
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 1. Zero occurrences of the character before '*'
                    dp[i][j] = dp[i][j - 2]
                    
                    # 2. One or more occurrences if the preceding character matches s[i - 1]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    # Match single character or '.'
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                        
        return dp[m][n]
        