class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash = {}
        idx = 0

        for x in nums:
            hash[x] = hash.get(x, 0) + 1
            if hash[x] <= 2:
                nums[idx] = x
                idx += 1

        return idx
