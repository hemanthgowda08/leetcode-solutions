class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_height = 0

        while left < right :
            width = right - left
            curr_height = min(height[left] , height[right])
            area = width * curr_height
            max_height = max(area,max_height)

            if height[left] < height[right] :
                left += 1
            else:
                right -= 1

        return max_height