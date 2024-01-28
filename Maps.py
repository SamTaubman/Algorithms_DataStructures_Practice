#Map implemented using a dictionary in python
mapp = {}

#Map implemented using a Hashtable/Hashmap
class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def _hash(self, key):
        # Simple hash function to compute the index
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def remove(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return

# Example usage:
my_map = HashTable()

# Adding key-value pairs
my_map.put('name', 'Alice')
my_map.put('age', 30)
my_map.put('city', 'New York')

# Retrieving values
print("Name:", my_map.get('name'))
print("Age:", my_map.get('age'))
print("City:", my_map.get('city'))

# Removing a key-value pair
my_map.remove('age')

#Map implemented using BST -> called a Treemap (this is a basic BST not necessarily balanced)
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if not node:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        return node

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if not node:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        return node.value

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
            if not node.right:
                return node.left

            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.value = min_node.value
            node.right = self._remove(node.right, min_node.key)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

# Example usage:
my_map = TreeMap()

# Adding key-value pairs
my_map.put('name', 'Alice')
my_map.put('age', 30)
my_map.put('city', 'New York')

# Retrieving values
print("Name:", my_map.get('name'))
print("Age:", my_map.get('age'))

# Checking if a key exists
print("Country:", my_map.get('country'))

# Removing a key-value pair
my_map.remove('age')

# Checking if a key exists after removal
print("Age:", my_map.get('age'))
