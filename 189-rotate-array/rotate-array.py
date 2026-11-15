class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        result = [0] * n

        for i in range(n):
            result[(i + k) % n] = nums[i]

        nums[:] = result