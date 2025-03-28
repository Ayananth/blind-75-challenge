class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_values = dict()
        for idx, value in enumerate(nums):
            search_val = target-value
            if search_val in prev_values:
                return [prev_values[search_val], idx]
            prev_values[value] = idx