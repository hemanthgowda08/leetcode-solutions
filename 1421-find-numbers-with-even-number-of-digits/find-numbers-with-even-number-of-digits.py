# class Solution(object):
#     def findNumbers(self, nums):
#        even_count = 0

#        for num in nums:
#             d = len(str(num))

#             if d % 2 == 0:
#                 even_count += 1


#         return even_count

class Solution(object):
    def findNumbers(self, nums):
        even_count = 0

        for num in nums:
            d = len(str(num))

            if d % 2 == 0:
                even_count += 1

        return even_count
