public class Solution {
    public bool ValidPalindrome(string s) {

        
        int low=0;
        int high=s.Length-1;

        while(low<=high){
            if (s[low]!=s[high]){
                return (check_palindrome(s,low+1,high) || check_palindrome(s,low,high-1));
            }

            low+=1;
            high-=1;
        }
        return true;
        
    }

    public bool check_palindrome(string s,int low,int high){

            while(low<=high){
                if (s[low]!=s[high]){
                    return false;
                }
                low+=1;
                high-=1;
            }
            return true;
        }

}