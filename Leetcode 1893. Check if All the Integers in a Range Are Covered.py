class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [x for x in range(left, right + 1)]
        for i in range(len(ranges)):
            start, end = ranges[i][0], ranges[i][1]
            for num in range(start, end + 1):
                if num in arr:
                    arr.remove(num)
        if arr == []:
            return True
        else:
            return False

                

                
