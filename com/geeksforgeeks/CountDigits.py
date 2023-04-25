"""
https://practice.geeksforgeeks.org/problems/count-digits5716/1
"""


class Solution:
    def evenlyDivides(self, N):
        count = 0
        num = N
        while N:
            val = N % 10
            if val and num % val == 0:
                count += 1
            N //= 10

        return count


if __name__ == "__main__":
    print(Solution().evenlyDivides(23))
