class Solution(object):
    def removeCoveredIntervals(self, intervals):

        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        maxEnd = 0

        for interval in intervals:

            start = interval[0]
            end = interval[1]

            if end > maxEnd:
                count += 1
                maxEnd = end

        return count