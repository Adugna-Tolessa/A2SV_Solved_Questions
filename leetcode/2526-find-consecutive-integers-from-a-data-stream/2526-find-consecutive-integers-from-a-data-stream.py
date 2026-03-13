class DataStream:

    def __init__(self, value: int, k: int):
        self.store = deque()
        self.value = value
        self.k = k
        self.cnt = 0

    def consec(self, num: int) -> bool:
        if len(self.store) == self.k:
            if self.store[0] == self.value:
                self.cnt -= 1
            self.store.popleft()
        self.store.append(num)
        if num == self.value:
            self.cnt += 1
        return self.cnt == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)