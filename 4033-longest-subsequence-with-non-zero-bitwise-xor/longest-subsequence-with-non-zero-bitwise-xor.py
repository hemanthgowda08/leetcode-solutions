class Solution(object):
    def longestSubsequence(self, nums):
        ans = 0
        for num in nums :
            ans ^= num

        if ans != 0 :
            return len(nums)

        for num in nums :
            if num != 0 :
                return len(nums) - 1

        return ans

        