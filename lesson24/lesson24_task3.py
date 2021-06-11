class Stack:
    def __init__(self):
        self.items = []

    # O(1)
    def is_empty(self):
        return self.items == []

    # O(1)
    def push(self, item):
        self.items.append(item)

    # O(1)
    def pop(self):
        return self.items.pop()

    # O(1)
    def peek(self):
        return self.items[-1]

    # O(n)
    def size(self):
        return len(self.items)

    # O(1)
    def get_from_stack(self, element):
        try:
            return self.items.pop(self.items.index(element))
        except ValueError:
            raise ValueError("There is no such an element in stack")


class Queue:
    def __init__(self):
        self.items = []

    # O(1)
    def is_empty(self):
        return self.items == []

    # O(n)
    def enqueue(self, item):
        self.items.insert(0, item)

    # O(1)
    def dequeue(self):
        return self.items.pop()

    # O(n)
    def size(self):
        return len(self.items)

    # O(1)
    def get_from_queue(self, element):
        try:
            return self.items.pop(self.items.index(element))
        except ValueError:
            raise ValueError("There is no such an element in queue")


if __name__ == '__main__':
    some_stack = Stack()
    some_queue = Queue()

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        some_stack.push(i)
        some_queue.enqueue(i)

    print(some_stack.get_from_stack(3))
    print(some_queue.get_from_queue(42))
