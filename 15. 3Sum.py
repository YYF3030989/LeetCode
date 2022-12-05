from itertools import combinations

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n, z, p = [], [], []
        r = set()
        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)

        if len(z) > 2:
            r.add((0, 0, 0))

        N = set(n)
        P = set(p)
        
        if z:
            for a in P:
                if (-1*a in N):
                    r.add((-1*a, 0, a))


        for x, y in combinations(n, 2):
            if -(x + y) in P:
                r.add(tuple(sorted([x, y, -(x + y)])))

        for x ,y in combinations(p, 2):
            if -(x + y) in N:
                r.add(tuple(sorted([x, y, -(x + y)])))
        # for i in range(len(p)):
        #     for j in range(i + 1, len(p)):
        #         add = -1*(p[i] + p[j])
        #         if (add in N):
        #             r.add(tuple(sorted([add, p[i], p[j]])))

        # for i in range(len(n)):
        #     for j in range(i + 1, len(n)):
        #         add = -1*(n[i] + n[j]) 
        #         if (add in P):
        #             r.add(tuple(sorted([n[i], n[j], add])))

        return r

s = Solution()
print(s.threeSum([1,1,-2]))