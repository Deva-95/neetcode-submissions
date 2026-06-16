class MyHashSet:

    def __init__(self):
        #self.dict = []
        self.data = [False]*1000000

    def add(self, key: int) -> None:
        #if key not in self.dict:
         #   self.dict.append(key)
        self.data[key] = True

    def remove(self, key: int) -> None:
        #if key in self.dict:
         #   self.dict.remove(key)
        self.data[key]=False
    def contains(self, key: int) -> bool:
        #return key in self.dict
        return self.data[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)