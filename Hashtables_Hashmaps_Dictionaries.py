#Hashmap Implementation w/ open addressing
class Pair: 
    def __init__(self, key, val):
        self.key = key
        self.val = val

class Hashmap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
    
    def hash(self, key):
        index = 0
        #The ord() function returns the number representing the unicode code of a specified character.
        for c in key:
            index += ord(c)
        return index % self.capacity

    def get(self, key):
        index = self.hash(key)
        
        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            
            index += 1
            index = index % self.capacity
    
    def remove(self, key):
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                # Removing an element using open-addressing actually causes a bug,
                # because we may create a hole in the list, and our get() may 
                # stop searching early when it reaches this hole.
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
    
    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)


#Hashmap Implementation w/ chaining
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = ListNode(key, value)
        else:
            current = self.hash_table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.hash_table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key not found: {key}")

    def delete(self, key):
        index = self._hash(key)
        current = self.hash_table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.hash_table[index] = current.next
                return
            prev = current
            current = current.next
        raise KeyError(f"Key not found: {key}")

    def __str__(self):
        result = []
        for node in self.hash_table:
            while node:
                result.append(f"({node.key}: {node.value})")
                node = node.next
        return "[" + ", ".join(result) + "]"

# Example usage
hash_map = HashMap(10)
hash_map.set("apple", 5)
hash_map.set("banana", 3)
print(hash_map.get("apple"))  # Output: 5
print(hash_map.get("banana"))  # Output: 3
hash_map.delete("banana")
print(hash_map.get("banana"))  # Raises KeyError: Key not found: banana