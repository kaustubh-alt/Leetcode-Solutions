from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ab = Counter(s)
        cd = Counter(t)
        ab = sorted(ab.items(),key=lambda x:x[0])
        cd = sorted(cd.items(),key=lambda y:y[0])
        return ab == cd
