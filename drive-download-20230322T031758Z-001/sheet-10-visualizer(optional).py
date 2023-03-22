from random import shuffle
# pip install binarytree==5.1.0
from binarytree import NodeNotFoundError, LEFT, RIGHT, _build_tree_string


class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    # In[3]:


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def search(self, key):
        temp = self._search(key, self.root)
        if temp:
            return temp.value
        return None

    def _search(self, key, cur):
        if cur == None:
            return None
        if cur.key == key:
            return cur
        elif key > cur.key:  # KEY=100 ############## CUR: 50 <<< 90 >>> 150
            return self._search(key, cur.right)  # go right
        else:  # KEY=60 ############## CUR: 50 <<< 90 >>> 150
            return self._search(key, cur.left)

    def add(self, key, value):
        if self.root == None:
            self.root = TreeNode(key, value)
            self.size += 1
        else:
            node = self._search(key, self.root)
            if node != None:
                node.value = value  # override value
            else:
                self._add(key, value, self.root)
                self.size += 1

    def _add(self, key, value, cur):
        if key < cur.key:  # KEY=60 ############## CUR: 50 <<< 90 >>> 150
            if cur.left != None:
                self._add(key, value, cur.left)
            else:  # a vacancy at cur.left
                cur.left = TreeNode(key, value)
        else:  # KEY=100 ############## CUR: 50 <<< 90 >>> 150
            if cur.right != None:
                self._add(key, value, cur.right)
            else:  # a vacancy at cur.right
                cur.right = TreeNode(key, value)


def tree_depth(root):
    if root:
        return 1 + max(tree_depth(root.left), tree_depth(root.right))
    else:
        return 0


def get_nodes_list(root):
    size = tree_depth(root)
    balanced_size = 1 << size
    balanced_tree_list = [None for _ in range(balanced_size)]

    def traverse(root, idx=0):
        if root:
            value = str(root.key) + "," + root.value
            value = str(root.key)  # + "," + root.value
            value = "[{}]".format(value)
            balanced_tree_list[idx] = value
            traverse(root.left, idx * 2 + 1)
            traverse(root.right, idx * 2 + 2)

    traverse(root)
    return balanced_tree_list


class DrawNode:
    def __init__(self, value, left=None, right=None):
        self.value = self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node({})'.format(self.val)

    def __str__(self):
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))


def draw_tree(values):
    nodes = [None if v is None else DrawNode(v) for v in values]

    for index in range(1, len(nodes)):
        node = nodes[index]
        if node is not None:
            parent_index = (index - 1) // 2
            parent = nodes[parent_index]
            if parent is None:
                raise NodeNotFoundError(
                    'parent node missing at index {}'.format(parent_index))
            setattr(parent, LEFT if index % 2 else RIGHT, node)

    return nodes[0] if nodes else None


step = 0


def inorder(root):
    # L M R
    if root != None:
        inorder(root.left)
        print((root.key), end=" ")  # , root.value
        inorder(root.right)


def add_with_draw(key, value, draw):
    global step
    # Builidng the binary tree
    bst.add(key, value)
    if draw:
        binary_tree_draw = draw_tree(get_nodes_list(bst.root))
        print("=" * 50, "\n", 'Step {} : Adding [ {} ]\n'.format(step, "{},{}".format(key, value)),
              binary_tree_draw)
        inorder(bst.root)
        print()
    step += 1


DRAW_ALL_STEPS = True
params = ([(90, "datastructure", DRAW_ALL_STEPS),
           (50, "conversion", DRAW_ALL_STEPS),
           (150, "electronics ", DRAW_ALL_STEPS),
           (20, "math", DRAW_ALL_STEPS),
           (75, "microprocessor", DRAW_ALL_STEPS),
           (95, "AI ", DRAW_ALL_STEPS),
           (175, "programming", DRAW_ALL_STEPS),
           (5, "operating systems", DRAW_ALL_STEPS),
           (25, "compiler", DRAW_ALL_STEPS),
           (66, "circuits", DRAW_ALL_STEPS),
           (80, "logic", DRAW_ALL_STEPS),
           (92, "control ", DRAW_ALL_STEPS),
           (111, "database", DRAW_ALL_STEPS),
           (166, "software engineering ", DRAW_ALL_STEPS),
           (200, "computer graphics", True),
           ])
print("="*50)
print("="*50)
print("="*50)
print("Inserting them in the right order (waves)")
bst = BinarySearchTree()
for param in params:
    add_with_draw(*param)
print("="*50)
print("="*50)
print("="*50)
print("Shuffling them")
shuffle(params)
bst = BinarySearchTree()
for param in params:
    add_with_draw(*param)
bst = BinarySearchTree()
print("="*50)
print("="*50)
print("="*50)
print("Sorting them")
params.sort(key=lambda item: item[0])
print(params)
print("="*50)
print("="*50)
print("="*50)
for param in params:
    add_with_draw(*param)
