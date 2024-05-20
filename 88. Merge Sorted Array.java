class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        for (int i = m + n - 1; m > 0 && n > 0; i--){
            if(nums1[m - 1] < nums2[n - 1]){
                nums1[i] = nums2[n - 1];
                n -= 1;
            }
            else{
                nums1[i] = nums1[m - 1];
                m -= 1;
            }
        }
        for (int i = 0; i < n; i++){
            nums1[i] = nums2[i];
        }
    }
}