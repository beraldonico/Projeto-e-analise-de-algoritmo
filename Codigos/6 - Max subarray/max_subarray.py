import json
import math

def find_max_crossing_subarray(data, low, mid, high):
    left_sum = float("-inf")
    sum = 0
    max_left = mid
    for i in range(mid, low, -1):
        sum += data[i]
        if sum > left_sum:
            left_sum = sum
    right_sum = float("-inf")
    sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high):
        sum += data[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return [max_left, max_right, left_sum + right_sum]

def find_max_subarray(data, low, high):
    if high == low:
        return [low, high, data[low]]
    else:
        mid = math.floor((low + high)/2)
        [left_low, left_high, left_sum] = find_max_subarray(data, low, mid)
        [right_low, right_high, right_sum] = find_max_subarray(data, mid + 1, high)
        [cross_low, cross_high, cross_sum] = find_max_crossing_subarray(data, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low, left_high, left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low, right_high, right_sum]
        else:
            return [cross_low, cross_high, cross_sum]

info = input()
data = json.loads(info)
result = find_max_subarray(data, 0, len(data) - 1)
print(round(result[2]))