class Solution {
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        res(nums, 0, nums.length - 1);
        res(nums, 0, k-1);
        res(nums, k, nums.length - 1);
        }
    public void res(int a[], int s, int e){
        while(s < e){
            int ext = a[e];
            a[e] = a[s];
            a[s] = ext;
            s++;
            e--;
        }
    }
}