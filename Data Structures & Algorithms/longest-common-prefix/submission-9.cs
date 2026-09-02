public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        
        Array.Sort(strs);

        string first=strs[0];
        string last=strs[strs.Length-1];

        string res="";

        for (int idx=0; idx<first.Length; idx++){
            if (first[idx]!=last[idx]){
                break;
            }
            res+=first[idx];
        }
        return res;
    }
}