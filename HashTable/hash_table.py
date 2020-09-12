class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        c = 0
        for char in key:
            c+= ord(char)

        print(c% self.max)

        return c % self.max

    def __setitem__(self, key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        print('has value',h)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        del self.arr[h]

# Driver code
t = HashTable()
t['one'] = 10
print(t['one'])
del t['one']
print(t['one'])
