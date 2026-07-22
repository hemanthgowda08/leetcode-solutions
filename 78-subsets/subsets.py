class Solution(object):
    def subsets(self, nums):
        result = []

        def backtrack(index, subset):
            if index == len(nums):
                result.append(subset[:])
                return

            subset.append(nums[index])
            backtrack(index + 1, subset)

            subset.pop()
            backtrack(index + 1, subset)

        backtrack(0, [])
        return result