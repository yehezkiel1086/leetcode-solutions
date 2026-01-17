# O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         #idx_l = 0
#         #idx_r = 1

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, x in enumerate(nums):
            if target - x in pair_idx:
                return [i, pair_idx[target - x]]
            pair_idx[x] = i
        