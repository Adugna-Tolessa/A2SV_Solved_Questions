"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        store = defaultdict(list)
        for emp in employees:
            store[emp.id] = emp
        def bfs(id):
            q = deque([id])
            tot = 0
            while q:
                emp_id = q.popleft()
                emp = store[emp_id]
                tot += emp.importance
                for sub in emp.subordinates:
                    q.append(sub)
            return tot
        return bfs(id)