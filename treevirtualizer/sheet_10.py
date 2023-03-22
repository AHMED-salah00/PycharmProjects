# ***
# **1)** Write a Python program that implements a Binary Search Tree (BST) which includes:
#
#     a) a function for inserting a key in the BST.
#     b) a function to search for a given key in the BST


class TreeNode:
    def __init__(self, key, value):
        self.key = key  # used for searching
        self.value = value  # TODO | Do we have to have a value?
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0  # TODO | can you get the tree size using recursion :D ?
        # TODO | can you find the maximum using recursion?
        # TODO | can you find the sum using recursion?

    def search(self, key):
        # wrapper around recursive search
        temp = self._search(key, self.root)
        if temp:  # found
            return temp.value
        # not found
        return None

    def _search(self, key, cur):
        """
        :param key: similar to cur.key
        :param cur: a tree node
        :return:
        """
        if cur is None:  # not found
            return None
        if cur.key == key:  # found
            return cur
        elif key > cur.key:  # KEY=100 ############## CUR: 50 <<< 90 >>> 150
            return self._search(key, cur.right)  # go right
        else:  # KEY=60 ############## CUR: 50 <<< 90 >>> 150
            return self._search(key, cur.left)

    def add(self, key, value):
        if self.root is None:  # TODO self.size == 0
            # if the tree is empty (first add)
            self.root = TreeNode(key, value)
            self.size += 1
        else:
            # if the tree is not empty
            node = self._search(key, self.root)
            if node is None:
                # I'm sure the value is not in the tree
                # wrapper around recursive add
                self._add(key, value, self.root)
                self.size += 1
            else:
                # found
                node.value = value  # override value TODO| we may convert the value into a list object and add more values instead of overriding!

    def _add(self, key, value, cur):
        if key < cur.key:  # cur.key = 90 , key = 60
            if cur.left is None:
                # a vacancy at cur.left
                # KEY=60 ############## CUR: None <<< |90| >>> 150
                cur.left = TreeNode(key, value)
            else:
                # KEY=60 ############## CUR: 70 <<< |90| >>> 150
                self._add(key, value, cur.left)
        elif cur.right is None:
            # a vacancy at cur.right
            # KEY=100 ############## CUR: 50 <<< 90 >>> None
            cur.right = TreeNode(key, value)
        else:
            # KEY=100 ############## CUR: 50 <<< 90 >>> 150
            self._add(key, value, cur.right)


# TODO| how we can trace those waves? (out of the scope of this course, see you in AI class :D)
# TODO| if we shuffle the inputs order randomly, do we get a balanced tree? is it bad?
# TODO| what if we sorted the inputs and added them one by one? do we get a balanced tree? is it bad? (WORST!)

bst = BinarySearchTree()
# you have to add those nodes in the same order as given below

# 1st wave
bst.add(90, "datastructure")

# 2nd wave
bst.add(50, "conversion")
bst.add(150, "electronics ")

# 3rd wave
bst.add(20, "math")
bst.add(75, "microprocessor")
bst.add(95, "AI ")
bst.add(175, "programming")

# 4th wave
bst.add(5, "operating systems")
bst.add(25, "compiler")
bst.add(66, "circuits")
bst.add(80, "logic")
bst.add(92, "control ")
bst.add(111, "database")
bst.add(166, "software engineering ")
bst.add(200, "computer graphics")

print(bst)


def inorder(root):
    # L M R
    if root is not None:
        inorder(root.left)
        # print(f"|{root.key}: {root.value}|", end=" ")  # , root.value
        print(root.key, end=" ")  # , root.value
        inorder(root.right)


inorder(bst.root)
print("")


def post_order(root):
    # L R M
    if root is not None:
        post_order(root.left)
        post_order(root.right)
        print(root.key, end=" ")  # , root.value


post_order(bst.root)
print("")


def pre_order(root):
    # M L R
    if root is not None:
        print(root.key, end=" ")  # , root.value
        pre_order(root.left)
        pre_order(root.right)


pre_order(bst.root)
print("")
