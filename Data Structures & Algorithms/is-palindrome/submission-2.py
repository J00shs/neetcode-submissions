class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0 #start of string
        R = len(s) - 1 #end of string
        
        while L < R:
            if not s[L].isalnum(): #check if L is A-Z,a-z,numbers
                L += 1
                continue
            if not s[R].isalnum(): #check if R is A-Z,a-z,numbers
                R -= 1
                continue
            if s[L].upper() == s[R].upper(): #compare 
                L += 1
                R -= 1
            elif s[L].upper() != s[R].upper():
                return False
        return True    
        
 
