class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash(self,key):
        c = 0
        for char in key:
            c+= ord(char)

        return c % self.max  # Modulus operator returns remainder, used as index.

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) ==2 and element[0] == key:
                found = True
                self.arr[h][idx] = (key,value)
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        # print(self.arr[h])
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print("deleting index", key)
                del self.arr[h][idx]


# Driver code
t = HashTable()

t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
print(t['march 6'])
del t['march 6']
