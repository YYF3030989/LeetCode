class Solution:
    def myAtoi(self, s: str) -> int:
        l = list(s.strip())
        if len(l) == 0:
            return 0
        
        sign = -1 if l[0] == "-" else 1
        if l[0] in ['-', "+"]: del l[0]
        a, i = 0, 0
        while i in range(len(l)) and l[i].isdigit():
            a = a * 10 + int(l[i])
            i += 1
            print (a)
        return max(-2 ** 31, min(a * sign, 2 ** 31 - 1))
