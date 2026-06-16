class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1  # 2147483647
        min_int = -2**31     # -2147483648

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10

            # Check overflow before appending digit
            if res > max_int // 10 or (res == max_int // 10 and digit > max_int % 10):
                return 0

            res = res * 10 + digit

        return sign * res