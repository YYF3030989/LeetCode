class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if (s == null || len(s) < 1):
        #     return "";

        def expandAroundCenter(s, left, right):
            L = left
            R = right
            while (L >= 0 and R < len(s) and s[L] == s[R]):
                L = L - 1
                R = R + 1
            return R - L - 1;


        b = 0
        e = 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if (length > e - b):
                b = i - int((length - 1) / 2)
                e = i + int(length / 2)

        return s[b : e + 1]


S = Solution()
result = S.longestPalindrome('abcb')
print(result)