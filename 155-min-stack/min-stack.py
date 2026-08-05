class MinStack(object):

    def __init__(self):
        self.items = []

    def push(self, value):
        if len(self.items) == 0:
            self.items.append([value, value])
        else:
            mini = min(self.items[-1][1], value)
            self.items.append([value, mini])

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[-1][0]

    def getMin(self):
        return self.items[-1][1]