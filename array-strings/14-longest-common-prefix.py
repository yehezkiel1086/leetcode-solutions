class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        n = len(pref)

        for x in strs[1:]:
            while pref != x[0:n]:
                n -= 1
                if n == 0:
                    return ""

                pref = pref[0:n]
        
        return pref