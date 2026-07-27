class Solution(object):
    def maxProduct(self, nums):
        # nums.sort()
        # large = nums[-1]
        # second = nums[-2]
        # return (large - 1) * (second - 1)

        largest = float('-inf')
        second = float('-inf')

        for num in nums :
            if num > largest :
                second = largest
                largest = num
            elif num > second :
                second = num

        return (largest - 1) * (second - 1) 
        