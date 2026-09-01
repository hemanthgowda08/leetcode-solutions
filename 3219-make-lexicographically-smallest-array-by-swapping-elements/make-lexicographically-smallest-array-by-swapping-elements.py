class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted((num, i) for i, num in enumerate(nums))
        n = len(nums)
        result = nums[:]

        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            values = [arr[i][0] for i in range(start, end + 1)]
            indices = [arr[i][1] for i in range(start, end + 1)]

            indices.sort()

            for i in range(len(values)):
                result[indices[i]] = values[i]

            start = end + 1

        return result