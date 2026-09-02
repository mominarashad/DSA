public class Solution {
    public int MajorityElement(int[] nums) {
         
         Dictionary<int,int> freq=new Dictionary<int,int>();

         foreach(int ch in nums){
            if(freq.ContainsKey(ch)){
                freq[ch]+=1;
            }
            else{
                freq[ch]=1;
            }
         }

         int max_frequency=0;
         int max_element=0;

         foreach( var item in freq){
                
                if (item.Value>max_frequency){
                    max_frequency=item.Value;
                    max_element=item.Key;
                }
         }
         return max_element;
    }
}