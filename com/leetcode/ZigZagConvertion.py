"""
https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        current_row = 0
        direction = 1

        for c in s:
            rows[current_row] += c

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)

if __name__=="__main__":
    print(Solution().convert("PAYPALISHIRING",3))