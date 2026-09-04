public class Solution {
    public string MergeAlternately(string word1, string word2) {

        int i=0;
        int j=0;

        int k=0;

        string res="";

        while (i<word1.Length && j<word2.Length){

              res+=word1[i];
              res+=word2[j];

              i++;
              j++;
              

        }
        while (i<word1.Length){

              res+=word1[i];

              i++;
             

        }
        while (j<word2.Length){

              res+=word2[j];

              j++;
             

        }
        return res;

        
    }
}