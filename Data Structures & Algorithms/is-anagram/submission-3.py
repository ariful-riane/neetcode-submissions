class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            d = {}
            for ch in s:
                if ch not in d:
                    d[ch] = 1
                else:
                    d[ch] += 1
            for ch in t:
                if ch not in d:
                    return False
                else:
                    d[ch] -= 1
            for key in d:
                if d[key] != 0:
                    return False
            return True
        else:
            return False
            