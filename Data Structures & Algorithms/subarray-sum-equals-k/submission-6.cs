public class Solution {
    public int SubarraySum(int[] nums, int k) {

        int prefix=0;
        int count=0;

        Dictionary<int,int> seen=new Dictionary<int,int>();
        seen[0]=1;

        foreach(int ch in nums){
            prefix+=ch;
            count+=seen.GetValueOrDefault(prefix-k,0);
            seen[prefix]=seen.GetValueOrDefault(prefix,0)+1;
        }
        return count;


        
    }
}