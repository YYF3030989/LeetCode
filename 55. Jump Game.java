class Solution {
    public boolean canJump(int[] nums) {
        int len = nums.length;
        int maxJump = 1;
        for (int i = 0; i < len; i++){
            if (maxJump < i + 1) { 
                return false;
            }

            if (maxJump < i + nums[i] + 1){
                maxJump = i + nums[i] + 1;
            }

            if (maxJump >= len){
                return true;
            }
        }
        return false;
    }
}