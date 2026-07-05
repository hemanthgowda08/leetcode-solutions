class Solution(object):
    def longestConsecutive(self, nums):
        my_set = set(nums)
        longest = 0

        for num in my_set:
            if num - 1 not in my_set:
                x = num
                count = 1

                while x + 1 in my_set:
                    x += 1
                    count += 1

                longest = max(longest, count)

        return longest