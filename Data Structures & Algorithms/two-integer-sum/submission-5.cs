public class Solution {
    public int[] TwoSum(int[] nums, int target) {
         
         Dictionary<int,int> freq=new Dictionary<int,int>();

         for (int idx=0; idx<=nums.Length; idx++){
            int val=nums[idx];
            int diff=target-val;

            if (freq.ContainsKey(diff)){
                return new int[]{freq[diff],idx};
            }

            freq[val]=idx;
         }

         return new int[] {};
    }
}
