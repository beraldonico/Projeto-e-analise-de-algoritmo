import json
import math

def construct(matrizR, matrizS, matrizT, matrizU, length):
    matriz = []
    for i in range(length):
        matriz.append([])
        for j in range(length):
            matriz[i].append(matrizR[i][j])
        for j in range(length):
            matriz[i].append(matrizS[i][j])

    for i in range(length):
        matriz.append([])
        for j in range(length):
            matriz[i + length].append(matrizT[i][j])
        for j in range(length):
            matriz[i + length].append(matrizU[i][j])
    return matriz

def subtration_matriz(matriz1, matriz2, length):
    matriz = []
    for i in range(length):
        matriz.append([])
        for j in range(length):
            matriz[i].append(matriz1[i][j] - matriz2[i][j])
    return matriz

def addition_matriz(matriz1, matriz2, length):
    matriz = []
    for i in range(length):
        matriz.append([])
        for j in range(length):
            matriz[i].append(matriz1[i][j] + matriz2[i][j])
    return matriz

def partition(matriz, length):
    matrizA = []
    matrizB = []
    matrizC = []
    matrizD = []
    new_length = math.floor(length/2)
    for i in range(new_length):
        matrizA.append([])
        for j in range(new_length):
            matrizA[i].append(matriz[i][j])

    for i in range(new_length):
        matrizB.append([])
        for j in range(new_length, length):
            matrizB[i].append(matriz[i][j])

    for i in range(new_length, length):
        matrizC.append([])
        for j in range(new_length):
            matrizC[i - new_length].append(matriz[i][j])

    for i in range(new_length, length):
        matrizD.append([])
        for j in range(new_length, length):
            matrizD[i - new_length].append(matriz[i][j])

    return [matrizA, matrizB, matrizC, matrizD]

def strassen(matriz1, matriz2, length):
    if length == 1:
        return [[matriz1[0][0] * matriz2[0][0]]]

    [matrizA, matrizB, matrizC, matrizD] = partition(matriz1, length)
    [matrizE, matrizF, matrizG, matrizH] = partition(matriz2, length)
    new_length = math.floor(length/2)
    
    P1 = strassen(matrizA, subtration_matriz(matrizF, matrizH, new_length), new_length)
    P2 = strassen(addition_matriz(matrizA, matrizB, new_length), matrizH, new_length)
    P3 = strassen(addition_matriz(matrizC, matrizD, new_length), matrizE, new_length)
    P4 = strassen(matrizD, subtration_matriz(matrizG, matrizE, new_length), new_length)
    P5 = strassen(addition_matriz(matrizA, matrizD, new_length), addition_matriz(matrizE, matrizH, new_length), new_length)
    P6 = strassen(subtration_matriz(matrizB, matrizD, new_length), addition_matriz(matrizG, matrizH, new_length), new_length)
    P7 = strassen(subtration_matriz(matrizA, matrizC, new_length), addition_matriz(matrizE, matrizF, new_length), new_length)

    matrizR = subtration_matriz(addition_matriz(P5, P4, new_length), subtration_matriz(P2, P6, new_length), new_length)
    matrizS = addition_matriz(P1, P2, new_length)
    matrizT = addition_matriz(P3, P4, new_length)
    matrizU = subtration_matriz(addition_matriz(P5, P1, new_length), addition_matriz(P3, P7, new_length), new_length)

    return construct(matrizR, matrizS, matrizT, matrizU, new_length)

def increase_matriz(matriz, length):
    if math.log(length, 2) % 1 == 0:
        return
    exp = math.ceil(math.log(length, 2))
    exp = 2 ** exp
    for i in range(length):
        for j in range(exp - length):
            matriz[i].append(0)
    for i in range(exp - length):
        matriz.append([])
        for j in range(exp):
            matriz[length + i].append(0)

def decrease_matriz(matriz, length):
    if len(matriz) == length:
        return matriz
    result = []
    for i in range(length):
        result.append([])
        for j in range(length):
            result[i].append(matriz[i][j])
    return result

info = input()
data = info.split(";")
matriz1 = json.loads(data[0])
matriz2 = json.loads(data[1])
init_length = len(matriz1)
increase_matriz(matriz1, init_length)
increase_matriz(matriz2, init_length)
result = strassen(matriz1, matriz2, len(matriz1))
print(decrease_matriz(result, init_length))
