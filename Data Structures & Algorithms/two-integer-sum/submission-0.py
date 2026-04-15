class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        long = len(nums)

        for i in range(long):
            for j in range(i + 1, long):
                if nums[i] + nums[j] == target:
                    return [i, j] 
        