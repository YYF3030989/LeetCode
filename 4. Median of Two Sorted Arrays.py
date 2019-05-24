class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) <= len(nums2):
            A = nums1;
            B = nums2;
        else:
            A = nums2;
            B = nums1;
        m = len(A);
        n = len(B);
        imin = 0;
        imax = m;
        while imin >= 0 and imax <= m:
            i = int((imin + imax)/2);
            j = int((m + n + 1)/2) - i;
            if i < m and B[j - 1] > A[i]:
                imin = i + 1;
            elif i > 0 and B[j] < A[i - 1]:
                imax = i - 1;
            else:

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1],B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i],B[j])

                return (max_of_left + min_of_right) / 2.0



S=Solution()
result = S.findMedianSortedArrays([1,2],[3,4])
# Solution.findMedianSortedArrays([1,2],[3])
print(result)