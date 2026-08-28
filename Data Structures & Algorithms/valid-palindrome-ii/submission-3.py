class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_palindrome(low,high):
            while low<=high:
                if s[low]!=s[high]:
                    return False

                low+=1
                high-=1

            return True

        low=0
        high=len(s)-1

        while low<=high:
            if s[low]!=s[high]:
                return check_palindrome(low+1,high) or check_palindrome(low,high-1)

            low+=1
            high-=1

        return True
