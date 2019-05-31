class Solution:
    def convert(self, s: str, numRows: int) -> str:
        print (len(s))
        if len(s) <= numRows:
            return s
        if numRows == 1:
            return s
        cyclelen = 2 * numRows - 2
        ret = ""
        for i in range(0, int((len(s) - 1) / cyclelen) + 1):
            ret += s[i * cyclelen]
        for j in range(1, numRows - 1):
            for k in range(1, int(len(s) / numRows + 1)):
                if int(cyclelen * k - (numRows - 1)) + (numRows - j - 1) < len(s):
                    ret += s[int(cyclelen * k - (numRows - 1)) - (numRows - j - 1)] + \
                           s[int(cyclelen * k - (numRows - 1)) + (numRows - j - 1)]
                elif (cyclelen * k - (numRows - 1)) - (numRows - j - 1) < len(s):
                    ret += s[int(cyclelen * k - (numRows - 1)) - (numRows - j - 1)]

        for l in range(int((len(s) - numRows)/cyclelen) + 1):
            ret += s[(cyclelen * l + (numRows - 1))]

        return ret


S = Solution()
result = S.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 3)
print(result)