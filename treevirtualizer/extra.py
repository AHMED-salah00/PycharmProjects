from sheet_10 import bst

print("from extra")


def size(current):
    if current:
        size_left = size(current.left)
        size_right = size(current.right)

        return size_left + size_right + 1
    return 0

print(size(bst.root))
