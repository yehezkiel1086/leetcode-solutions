class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0

        for x in t:
            if idx == len(s):
                return True
            if x == s[idx]:
                idx += 1
        
        return idx == len(s)