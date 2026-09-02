public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        
        Dictionary<string,List<string>> groups=new Dictionary<string,List<string>>();

        foreach( string words in strs){

            Dictionary<char,int> freq = new Dictionary<char,int>();

            foreach(char ch in words){

                if (freq.ContainsKey(ch)){
                    freq[ch]+=1;
                }
                else{
                    freq[ch]=1;
                }
            }


            string keys="";

            foreach(var items in freq.OrderBy(x=>x.Key)){
                keys+=items.Key + items.Value.ToString();
            }

            if (groups.ContainsKey(keys)){
                groups[keys].Add(words);
            }
            else{

                groups[keys]=new List<string>{words};
            }

        }

        return new List<List<String>>(groups.Values);
    }
}
