"""
https://leetcode.com/problems/reverse-integer/
"""


# class Solution {
# public int reverse(int x) {
# long rev=0;
#
#
# while (x != 0){
# rev=(rev * 10)+(x % 10);
# x /= 10;
#
# }
# return (Integer.MAX_VALUE < rev | | rev < Integer.MIN_VALUE) ? 0: (int)
# rev;
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        if rev < -2 ** 31 or rev > 2 ** 31 - 1:
            return 0
        else:
            return rev


