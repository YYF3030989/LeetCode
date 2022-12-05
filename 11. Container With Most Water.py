from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        hlength = len(height)
        left = 0
        right = hlength - 1
        water = 0
        while(left < right):
            water = max(water, (right - left) * min(height[left], height[right]))
            if (height[left] <= height[right]):
                left += 1
            else:
                right -= 1
        return water

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))