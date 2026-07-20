class Solution(object):
    def shiftGrid(self, grid, k):
        arr = []


        for rows in grid :
            for num in rows :
                arr.append(num)
        n = len(arr)
        k = k % n
        arr = arr[-k:] + arr[:-k]

        m = len(grid[0])
        result = []

        for i in range(0,n,m) :
            result.append(arr[i : i + m])

        return result


