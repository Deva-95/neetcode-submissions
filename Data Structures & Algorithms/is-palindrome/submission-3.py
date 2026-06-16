class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        s=s.lower()
        while(start<end):
            if s[start].isalnum():
                if s[end].isalnum():
                    if s[start]!=s[end]:
                        return False
                    start+=1
                    end-=1
                else:
                    end-=1
            else:
                start+=1
        return True
            