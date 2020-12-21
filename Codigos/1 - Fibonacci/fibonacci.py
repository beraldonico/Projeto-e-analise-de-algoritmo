# -*- coding: utf-8 -*-
import time

def fibonacci_i(N):
    data0 = 0
    data1 = 1
    i = N
    while i > 1:
        data0, data1 = data1, data0 + data1
        i -= 1
    return data1

def fibonacci_r(N):
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        return fibonacci_r(N - 1) + fibonacci_r(N - 2)

element = int(input("Elemento da sequencia Fibonacci: "))
time1 = time.time()
print("Elemento", element, "da squencia Fibonacci iterativa é: ", fibonacci_i(element))
time2 = time.time()
time3 = time.time()
print("Elemento", element, "da squencia Fibonacci recursiva é: ", fibonacci_r(element))
time4 = time.time()
print("Tempo decorrido do iterativo:", time2 - time1)
print("Tempo decorrido do recursivo:", time4 - time3)