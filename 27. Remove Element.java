class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        int n = nums.length;
        if (n ==0){
            return k;
        }
        for (int i=0; i < n - 1; i++){
            if (nums[i]!=val){
                k++;
            }else{
                nums[i] = nums[n-1];
                n--;
                i--;
            }
        }
        if (nums[n -1] != val){
            k++;
        }
        return k;
    }
}
