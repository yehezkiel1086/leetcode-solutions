class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}

        for x in s:
            hash_s[x] = hash_s.get(x, 0) + 1
        
        for x in t:
            if x not in hash_s or hash_s[x] <= 0:
                return False
            else:
                hash_s[x] -= 1
        
        return True