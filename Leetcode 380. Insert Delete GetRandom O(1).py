import random
class RandomizedSet:

    def __init__(self):
        self.store = defaultdict(int)
        self.arr = [] 
    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        self.store[val] = len(self.arr)
        self.arr.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
        idx = self.store[val]
        last = self.arr[-1]

        self.arr[idx] = last
        self.store[last] = idx
        self.arr.pop()
        del self.store[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)
