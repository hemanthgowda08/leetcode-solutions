class Solution(object):
    def maximumWeight(self, intervals):
        intervals = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        intervals.sort(key=lambda x: x[1])

        n = len(intervals)

        prev = [0] * n

        for i in range(n):
            l = intervals[i][0]
            left = 0
            right = i - 1

            while left <= right:
                mid = (left + right) // 2

                if intervals[mid][1] < l:
                    prev[i] = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, idx = intervals[i - 1]

            for k in range(1, 5):
                skip_score, skip_indices = dp[i - 1][k]

                take_score, take_indices = dp[prev[i - 1]][k - 1]
                take_score += w
                take_indices = sorted(take_indices + [idx])

                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)
                else:
                    dp[i][k] = min(
                        (take_score, take_indices),
                        (skip_score, skip_indices)
                    )

        best = (0, [])

        for k in range(1, 5):
            if dp[n][k][0] > best[0]:
                best = dp[n][k]
            elif dp[n][k][0] == best[0]:
                best = min(best, dp[n][k])

        return sorted(best[1])