import json

def selection_sort(pessoas, lenght):
    for j in range(lenght - 1):
        minimo = j
        for k in range(j + 1, lenght):
            if pessoas[k]["idade"] < pessoas[minimo]["idade"]:
                minimo = k

        pessoas[j], pessoas[minimo] = pessoas[minimo], pessoas[j]

data = input()  
pessoas = json.loads(data)
#print(pessoas)
selection_sort(pessoas, len(pessoas))
print(pessoas)