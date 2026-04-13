class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        long = len(nums)
        for i in range(long):
            for j in range(i + 1, long):
                if nums[i] == nums[j]:
                    return True
        return False

        