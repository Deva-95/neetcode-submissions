class Solution {
    public int hammingWeight(int n) {
        int k = 0;
        while(n>0){
            if((n&1)==1){
                k+=1;
            }
            n = n>>>1;
        }
        return k;
    }
}
