class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}

        for x in magazine:
            hash[x] = hash.get(x, 0) + 1
        
        for x in ransomNote:
            if x not in hash or hash[x] <= 0:
                return False
            hash[x] -= 1
        
        return True