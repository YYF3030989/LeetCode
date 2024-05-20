class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strg=str(x)
        if x > 0 and x < 2**31 - 1:
            rev = int(strg[::-1])
            # return rev
        elif x < 0 and x > -2**31:
            rev = int(strg[-1:0:-1]) * -1
            # return rev
        else:
            return (0)
        mina = -2**31  
        maxa = 2**31 - 1  
        if rev not in range(mina, maxa):  
            return 0  
        else:  
            return rev

x = 1534236469
Solution(x)