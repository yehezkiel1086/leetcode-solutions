class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_p = {}
        hash_s = {}

        arr = s.split(' ')

        if len(pattern) != len(arr):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hash_p:
                hash_p[pattern[i]] = i
            
            if arr[i] not in hash_s:
                hash_s[arr[i]] = i
            
            if hash_p[pattern[i]] != hash_s[arr[i]]:
                return False
        
        return True
