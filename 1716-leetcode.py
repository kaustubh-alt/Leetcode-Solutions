class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        mul = n//7
        rem = n%7

        ans += mul*28
        ans += sum(i*7 for i in list(range(1,mul)))
        ans += sum(i+mul for i in list(range(1,rem+1)))

        return ans
