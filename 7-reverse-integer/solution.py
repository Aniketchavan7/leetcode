class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0
        while x_abs != 0:
            pop = x_abs % 10
            x_abs //= 10
            rev = rev * 10 + pop
        res = sign * rev
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
