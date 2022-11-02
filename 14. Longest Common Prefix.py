class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if (strs[0] == ""):
            return ""
        ans = len(strs[0])
        for i in range(1, len(strs)):
            if (strs[i] == ""):
                return ""
            j = 0
            while ((j < len(strs[i])) and (j < len(strs[0])) and (strs[0][j] == strs[i][j])):

                j += 1
                print (i)
                print (j)
            ans = min(ans, j)

        return strs[0][0:ans]

solution = Solution()
print(solution.longestCommonPrefix(["ab", "abc", "abcc"]))