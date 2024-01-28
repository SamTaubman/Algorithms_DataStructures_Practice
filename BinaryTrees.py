#Binary Tree
class Node:

    def __init__(self, value = None):
        self.left  = None
        self.right = None
        self.value = value

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left  = n2
n1.right = n3

#Binary Search Tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.key = self._min_value_node(root.right).key

            # Delete the inorder successor
            root.right = self._remove(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        print(result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)

    # def inorder_traversal(self, node):
    #     result = []
    #     if not node:
    #         return
    #     self.inorder_traversal(node.left)
    #     result.append(node.key)
    #     self.inorder_traversal(node.right)
    #     return result



bst = BinarySearchTree()
bst.insert(5)
bst.insert(4)
bst.insert(2)
bst.insert(1)
bst.insert(9)
bst.insert(5)
bst.in_order_traversal()
bst.remove(5)
bst.in_order_traversal()
bst.remove(1)
bst.in_order_traversal()
