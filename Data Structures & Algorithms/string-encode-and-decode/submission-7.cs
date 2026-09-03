public class Solution {

    public string Encode(IList<string> strs) {

        string encoded="";

        foreach(string ch in strs){
            encoded+=ch.Length.ToString()+'#'+ch;
        }
        
        return encoded;
    }

    public List<string> Decode(string s) {

       int j=0;
       int i=0;
       List<String> res=new List<String>();
       while (i<s.Length){
            j=i;
            while (s[j]!='#'){
                j++;
            }

            int length=int.Parse(s[i..j]);
            int start=j+1;
            string value=s[start..(start+length)];
            res.Add(value);
            i=start+length;
        }

        return res;

   }
}
