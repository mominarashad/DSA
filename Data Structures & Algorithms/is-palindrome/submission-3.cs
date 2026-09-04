public class Solution {
    public bool IsPalindrome(string s) {

        string cleaned="";

        foreach(char ch in s){

            if (char.IsLetterOrDigit(ch)){
                cleaned+=char.ToLower(ch);
            }
        }

        int low=0;
        int high=cleaned.Length-1;

        while (low<=high){
            if (cleaned[low]!=cleaned[high]){
                return false;
            }

            low+=1;
            high-=1;
        }
        return true;
        
    }
}
