class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        ans = 0
        check = skill[-1] + skill[0]
        while l < r:
            if skill[r] + skill[l] == check:
                ans += (skill[r] * skill[l])
                l += 1
                r -= 1
            else:
                return -1
                break
        return ans
