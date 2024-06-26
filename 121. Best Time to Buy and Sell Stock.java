class Solution {
    public int maxProfit(int[] prices) {
        int ret = 0;
        int min = prices[0];
        for (int i = 1; i < prices.length; i++){
            if (prices[i] - min > ret){
                ret = prices[i] - min;
            }
            if (prices[i] < min){
                min = prices[i];
            }
        }
        return ret;
    }
}