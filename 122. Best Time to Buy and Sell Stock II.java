class Solution {
    public int maxProfit(int[] prices) {
        int sum = 0;

        for (int i = 0; i < prices.length - 1; i++){
            sum += (prices[i + 1] - prices[i] > 0 ? prices[i + 1] - prices[i] : 0);
        }
        return sum;
    }
}