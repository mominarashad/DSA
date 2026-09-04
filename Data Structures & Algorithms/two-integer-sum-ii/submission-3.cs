public class Solution {
    public int[] TwoSum(int[] numbers, int target) {

        Dictionary<int,int> freq=new Dictionary<int,int>();

        for (int i=0; i<numbers.Length; i++){
            int val=numbers[i];
            int diff=target-val;

            if (freq.ContainsKey(diff)){
                return new int[]{freq[diff]+1,i+1};
            }

            freq[val]=i;


        }
        return new int[]{};
        
    }
}
