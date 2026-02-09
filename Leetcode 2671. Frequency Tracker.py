# from collections import defaultdict()
class FrequencyTracker:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.freq_counts = defaultdict(int)
    def add(self, number: int) -> None:
        old_f = self.tracker[number]
        if old_f > 0:
            self.freq_counts[old_f] -= 1

        self.tracker[number] += 1
        new_f = self.tracker[number]
        self.freq_counts[new_f] += 1
        
    def deleteOne(self, number: int) -> None:
        if self.tracker[number] > 0:
            old_f = self.tracker[number]
            self.freq_counts[old_f] -= 1

            self.tracker[number] -= 1
            new_f = self.tracker[number]

            if new_f > 0:
                self.freq_counts[new_f] += 1
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_counts[frequency] > 0
