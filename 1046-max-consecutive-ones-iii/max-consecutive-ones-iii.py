class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        zeros = 0
        n = len(nums)
        maxi = 0

        while right < n :
            if nums[right] == 0 :
                zeros += 1

            while zeros > k :
                if nums[left] == 0 :
                    zeros -= 1
                left += 1

            if zeros <= k :
                maxi = max(right - left + 1, maxi)

            right += 1

        return maxi

