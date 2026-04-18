class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_streak = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                long = 1
                while long + num in set_nums:
                    long += 1
                
                longest_streak = max(long, longest_streak)
        return longest_streak

        