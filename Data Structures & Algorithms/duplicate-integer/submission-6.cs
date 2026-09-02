public class Solution {
    public bool hasDuplicate(int[] nums) {
        
        HashSet<int> set=new HashSet<int>();

        foreach(int ch in nums){
            if(set.Contains(ch)){
                return true;
            }

            set.Add(ch);
        }

        return false;
    }
}