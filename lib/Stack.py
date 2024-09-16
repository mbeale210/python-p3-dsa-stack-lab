class Stack:

    def __init__(self, items=None, limit=None):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) >= self.limit

    def search(self, target):
        for i, item in enumerate(reversed(self.items)):
            if item == target:
                return i
        return -1