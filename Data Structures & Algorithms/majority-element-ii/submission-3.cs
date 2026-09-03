public class Solution {
    public List<int> MajorityElement(int[] nums) {

        int n=nums.Length;

        List<int> res=new List<int>();

        Dictionary<int,int> freq=new Dictionary<int,int>();

        foreach(int ch in nums){
            if (freq.ContainsKey(ch)){
                freq[ch]+=1;
            }
            else{
                freq[ch]=1;
            }
        }

        foreach (var item in freq){
             
            if (item.Value>n/3){
                res.Add(item.Key);
            }
        }
        return res;
        
    }
}