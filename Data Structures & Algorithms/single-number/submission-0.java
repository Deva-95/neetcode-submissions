class Solution {
    public int singleNumber(int[] nums) {
        int k = 0;
        for(int x:nums){
            k^=x;
        }
        return k;
    }
}
