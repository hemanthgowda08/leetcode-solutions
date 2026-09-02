class Solution(object):
    def uniformArray(self, nums1):
        has_even = False
        has_odd = False

        for num in nums1:
            if num % 2 == 0:
                has_even = True
            else:
                has_odd = True

        return True