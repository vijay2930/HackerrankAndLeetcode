"""
https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
"""


def birthdayCakeCandles(candles):
    max_height = float('-inf')
    count_candle = {}
    for candle in candles:
        if candle in count_candle:
            count_candle[candle] += 1
        else:
            count_candle[candle] = 1
        if candle > max_height:
            max_height = candle
    return count_candle[max_height]


if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)
