class Solution(object):
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)

        while smallest :
            largest, smallest = smallest , largest % smallest

        return largest