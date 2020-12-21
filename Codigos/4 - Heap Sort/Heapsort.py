import json
import math

def max_heapify(heap, indice, heap_length):
    left = indice * 2 + 1
    right = indice * 2 + 2
    maximo = indice
    if left < heap_length and heap[left] > heap[indice]:
        maximo = left
    if right < heap_length and heap[right] > heap[maximo]:
        maximo = right
    if maximo != indice:
        heap[indice], heap[maximo] = heap[maximo], heap[indice]
        max_heapify(heap, maximo, heap_length)

def construct_HeapMax(data, length):
    heap = data
    heap_length = length
    for i in range(math.floor(length/2), 0, -1):
        max_heapify(heap, i - 1, heap_length)
    return heap

def Heap_sort(data, length):
    heap = construct_HeapMax(data, length)
    heap_length = length
    for k in range(length - 1, 0, -1):
       data[0], data[k] = data[k], data[0]
       heap_length -= 1
       max_heapify(heap, 0, heap_length)

data = input()
vetor = json.loads(data)
Heap_sort(vetor, len(vetor))
print(vetor)