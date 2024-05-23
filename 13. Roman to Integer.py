from unittest import result


class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        sum = 0
        chr_map = {'I': 1, 'V' : 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(length - 1):
            if (chr_map[s[i]] >= chr_map[s[i + 1]]):
                sum += chr_map[s[i]]
            else:
                sum -= chr_map[s[i]]

        sum += chr_map[s[-1]]
        return sum

s = Solution()
print(s.romanToInt("DXIX"))