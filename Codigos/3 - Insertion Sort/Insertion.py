import json

def insertion_sort(pessoas, length):
    for j in range(1, length):
        tmp = pessoas[j]
        k = j - 1
        while k >= 0 and pessoas[k]['idade'] > tmp['idade']:
            pessoas[k + 1] = pessoas[k]
            k -= 1

        pessoas[k + 1] = tmp

data = input()  
pessoas = json.loads(data)
insertion_sort(pessoas, len(pessoas))
print(pessoas)