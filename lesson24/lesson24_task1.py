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


if __name__ == '__main__':
    def reverse(some_str):
        stack = Stack()
        reverse_str = ''

        for i in some_str:
            stack.push(i)

        while not stack.is_empty():
            reverse_str += stack.pop()

        return reverse_str


    print(reverse("Testing"))
