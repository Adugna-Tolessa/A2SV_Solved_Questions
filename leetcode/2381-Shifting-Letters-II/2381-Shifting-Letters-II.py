class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0] * (len(s) + 1)
        pref = []

        for shift in shifts:
            if shift[2] == 0:
                temp[shift[0]] -= 1
                temp[shift[1] + 1] += 1
            else:
                temp[shift[0]] += 1
                temp[shift[1] + 1] -= 1

        for n in temp:
            if pref:
                pref.append(pref[-1] + n)
            else:
                pref.append(n)

        ans = ""
        for i in range(len(s)):
            t = chr((((ord(s[i]) - ord("a")) + pref[i]) % 26) + ord("a"))
            ans += t
        
        return ans