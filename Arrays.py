import ctypes

class Array:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, i):
        if not 0 <= i < self.size:
            return IndexError('i is out of bounds')
        return self.array[i]

    def append(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
 
        self.array[self.size] = element
        self.size += 1

    def delete(self):
        if self.size == 0:
            print("Array is empty deletion not Possible")
            return
 
        self.array[self.size-1] = 0
        self.size -= 1

    def insert(self, element, index):
        if index < 0 or index > self.size:
            print("please enter appropriate index..")
            return
 
        if self.size == self.capacity:
            self.resize(2*self.capacity)
 
        for i in range(self.size-1, index-1, -1):
            self.array[i+1] = self.array[i]
 
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        if self.size == 0:
            print("Array is empty deletion not Possible")
            return
 
        if index < 0 or index >= self.size:
            return IndexError("Index out of bound....deletion not possible")
 
        if index == self.size-1:
            self.array[index] = 0
            self.size -= 1
            return
 
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]
 
        self.array[self.size-1] = 0
        self.size -= 1

    def clear(self):
        if self.size == 0:
            return
        for i in range(0, self.size):
            self.array[i] = 0
        return
    
    def resize(self, new_capacity):
        array2 = self.make_array(new_capacity)
 
        for k in range(self.size):
            array2[k] = self.array[k]
 
        self.array = array2
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


array1 = Array()
array1.append(1)
print(array1)


