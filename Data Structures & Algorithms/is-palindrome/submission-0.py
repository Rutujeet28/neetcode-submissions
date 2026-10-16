class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return False
        
        right = 0
        left = len(s) - 1

        s = s.lower()

        while(right < left):
            if not s[right].isalnum():
                right += 1
                continue
            
            if not s[left].isalnum():
                left -= 1
                continue

            if s[right] != s[left]:
                return False
            
            right += 1
            left -= 1
            
        return True
        