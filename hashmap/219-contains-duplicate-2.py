class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}

        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i
            else:
                if abs(hash[nums[i]] - i) <= k:
                    return True
                else:
                    hash[nums[i]] = i

        return False