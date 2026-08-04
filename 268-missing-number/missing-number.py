class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        curr = n * (n + 1) // 2
        actual = sum(nums)
        return curr - actual

