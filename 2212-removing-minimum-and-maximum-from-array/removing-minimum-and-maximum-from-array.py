class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        option1 = right + 1
        option2 = n - left
        option3 = left + 1 + n - right

        return min(option1, option2, option3)