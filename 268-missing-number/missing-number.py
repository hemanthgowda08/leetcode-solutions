class Solution(object):
    def missingNumber(self, nums):
        # for i in range(0,len(nums)):
        #     if i not in nums:
        #         return i

        n = len(nums)
        current = n * (n + 1) // 2

        actual = sum(nums)
        return current - actual
        