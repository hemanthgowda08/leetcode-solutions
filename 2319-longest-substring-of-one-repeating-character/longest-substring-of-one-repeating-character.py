class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)

        def merge(node):
            left = tree[node * 2]
            right = tree[node * 2 + 1]

            left_char = left[0]
            right_char = right[1]

            prefix = left[2]
            suffix = right[3]
            best = max(left[4], right[4])

            if left[1] == right[0]:
                best = max(best, left[3] + right[2])

                if left[2] == left[5]:
                    prefix = left[5] + right[2]

                if right[3] == right[5]:
                    suffix = right[5] + left[3]

            tree[node] = [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                left[5] + right[5]
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = [s[l], s[l], 1, 1, 1, 1]
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            merge(node)

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = [char, char, 1, 1, 1, 1]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            merge(node)

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])

        return ans