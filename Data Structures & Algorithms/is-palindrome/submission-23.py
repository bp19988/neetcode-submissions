class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l<r and not self.alphaNum(s[l]):
                l+=1
            while r>l and not self.alphaNum(s[r]):
                r-=1

            if s[l].lower() != s[r].lower():
                return False
            l,r, = l+1, r-1
        return True
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        # want to lower case
        # want only numbers and letters
        # trim ws
        # want only read forward and backwards
        # newStr = ''
        # for ch in s:
        #     if ch.isalnum():
        #         newStr += ch.lower()
        # return newStr == newStr[::-1]

        # s = s.lower()
        # s = "".join(char for char in s if char.isalnum())
        # if s == s[::-1]:
        #     return True
        # else:
        #     return False
