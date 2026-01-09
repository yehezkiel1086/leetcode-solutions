class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        res = major = 0

        for x in nums:
            hash[x] = 1 + hash.get(x, 0)
            if hash[x] > major:
                major = hash[x]
                res = x
        
        return res