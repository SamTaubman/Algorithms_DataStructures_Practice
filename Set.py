#Implementing a Set using the set() function
x = set()
x.add()
x.remove()
x.update()
5 in x

#Implementing a Set as a Hashset
class Bucket:
    def __init__(self):
        self.bucket=[]

    def update(self, key):
        found=False
        for i,k in enumerate(self.bucket):
            if key==k:
                self.bucket[i]=key
                found=True
                break
        if not found:
            self.bucket.append(key)

    def get(self, key):
        for k in self.bucket:
            if k==key:
                return True
        return False
   
    def remove(self, key):
        for i,k in enumerate(self.bucket):
            if key==k:
                del self.bucket[i]

class MyHashSet:
    def __init__(self):
        self.key_space = 2096
        self.hash_table=[Bucket() for i in range(self.key_space)]

    def add(self, key):
        hash_key=key%self.key_space
        self.hash_table[hash_key].update(key)

    def remove(self, key):
        hash_key=key%self.key_space
        self.hash_table[hash_key].remove(key)

    def contains(self, key):
        hash_key=key%self.key_space
        return self.hash_table[hash_key].get(key)
    
#Implementing a Set using a Treeset
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class TreeSet:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _balance(self, node):
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def add(self, key):
        self.root = self._add(self.root, key)

    def _add(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._add(node.left, key)
        elif key > node.key:
            node.right = self._add(node.right, key)
        else:
            return node  # Duplicate keys are not allowed

        self._update_height(node)
        return self._balance(node)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._remove(node.right, min_node.key)

        self._update_height(node)
        return self._balance(node)

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def contains(self, key):
        return self._contains(self.root, key)

    def _contains(self, node, key):
        if not node:
            return False
        if key < node.key:
            return self._contains(node.left, key)
        elif key > node.key:
            return self._contains(node.right, key)
        else:
            return True

    def __str__(self):
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.key] + inorder_traversal(node.right)

        return str(inorder_traversal(self.root))