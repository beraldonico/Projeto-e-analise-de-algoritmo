import json
import math

def quicksort(data, low, high):
    if low < high:
        pivot = partition(data, low, high)
        quicksort(data, low, pivot)
        quicksort(data, pivot + 1, high)

def partition(data, low, high):
    pivot = data[low + math.floor((high - low)/2)]
    start = low - 1
    end = high + 1
    while True:
        while True:
            start += 1
            if data[start] >= pivot:
                break
        while True:
            end -= 1
            if data[end] <= pivot:
                break
        if start >= end:
            return end
        data[start], data[end] = data[end], data[start]

info = input()
data = json.loads(info)
quicksort(data, 0, len(data) - 1)
print(data)