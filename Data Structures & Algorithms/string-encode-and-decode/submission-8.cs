public class Solution {

    public string Encode(IList<string> strs) {
        string encoded="";

        foreach (string str in strs){
            encoded+=str.Length.ToString()+'#'+str;
        }
        return encoded;
    }

    public List<string> Decode(string s) {

        int i=0;
        int j=0;

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
