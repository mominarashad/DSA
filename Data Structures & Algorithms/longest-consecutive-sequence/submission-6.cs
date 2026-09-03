public class Solution {
    public int LongestConsecutive(int[] nums) {

        HashSet<int> set=new HashSet<int>();

        for (int i=0; i<nums.Length; i++){
            set.Add(nums[i]);
        }
        int max_length=0;
        foreach (int ch in set){
            if (!set.Contains(ch-1)){
                int length=0;

                while (set.Contains(ch+length)){
                    length+=1;
                }

                max_length=Math.Max(max_length,length);
            }
        }

        return max_length;
        
    }
}
