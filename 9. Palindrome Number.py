class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        xlength = len(xstr)

        for i in range(xlength//2):
            if xstr[i] != xstr[-1-i]:
                return False
        return True
        


s= Solution()
print(s.isPalindrome(989))