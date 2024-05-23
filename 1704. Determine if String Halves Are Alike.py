from pickle import TRUE


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        leng = int(len(s) / 2)
        a = s[:leng]
        b = s[leng :]
        print (a)
        print (b)
        al = 0
        bl = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(leng):
            if (a[i] in vowels):
                al += 1
            if (b[i] in vowels):
                bl += 1
        print ("al = %s" % al)
        print ("bl = %s" % bl)
        if al == bl:
            return True
        else:
            return False

s = Solution()
print(s.halvesAreAlike('textbook'))