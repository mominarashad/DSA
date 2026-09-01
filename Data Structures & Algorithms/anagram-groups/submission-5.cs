public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        
        Dictionary<string,List<string>> groups=new Dictionary<string,List<string>>();

        foreach (string words in strs){

            Dictionary<char,int> freq=new Dictionary<char,int>();

            foreach(char ch in words){
                
                if (freq.ContainsKey(ch)){
                    freq[ch]+=1;
                }
                else{
                    freq[ch]=1;
                }
            }

            string key="";

            foreach (var items in freq.OrderBy(x=>x.Key)){
                key+=items.Key+items.Value.ToString();
            }

            if (groups.ContainsKey(key)){
                groups[key].Add(words);
            }
            else{
                groups[key]=new List<string>{words};
            }
        }
        return new List<List<string>>(groups.Values);
    }
}
