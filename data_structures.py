class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class BinaryTree:
    def __init__(self, Data):
        self.key = Data
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertright(self, newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

