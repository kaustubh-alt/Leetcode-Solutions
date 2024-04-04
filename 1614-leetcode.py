class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        ls = []
        for i in s:
            if i == "(":
                ans += 1
            elif i == ")":
                ans -= 1

            ls.append(ans)
        
        return max(ls)

        
