class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        first = -1
        last = -1
        minDistance = float('inf')
        index = 1

        prev = head
        curr = head.next

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                if first == -1:
                    first = index
                else:
                    minDistance = min(minDistance, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if first == last:
            return [-1, -1]

        maxDistance = last - first

        return [minDistance, maxDistance]