class Solution:
    def isPalindrome(self, s: str) -> bool:
        # want to lower case
        # want only numbers and letters
        # trim ws
        # want only read forward and backwards
        
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        if s == s[::-1]:
            return True
        else:
            return False
