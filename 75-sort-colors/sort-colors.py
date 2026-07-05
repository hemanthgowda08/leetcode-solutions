class Solution(object):
    def sortColors(self, nums):
        color0 = 0
        color1 = 0
        color2 = 0

        for num in nums:
            if num == 0 :
                color0 += 1
            elif num == 1 :
                color1 += 1
            else:
                color2 += 1

        index = 0

        for i in range(color0):
            nums[index] = 0
            index += 1

        for i in range(color1):
            nums[index] = 1
            index += 1
        
        for i in range(color2):
            nums[index] = 2
            index += 1

        