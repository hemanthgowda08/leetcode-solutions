class Solution(object):
    def uniformArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for num in nums1:
            if num % 2 == 0:
                min_even = min(min_even, num)
            else:
                min_odd = min(min_odd, num)

        if min_odd == float('inf') or min_even == float('inf'):
            return True

        return min_odd < min_even