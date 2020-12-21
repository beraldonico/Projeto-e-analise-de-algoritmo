# -*- coding: utf-8 -*-
import sys

class tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def size_file(data):
    size = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            size += 1
    size *= 8
    return size

def frequency(data):
    table = [[], []]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in table[0]:
                table[0].append(data[i][j])
                table[1].append(1)
            else:
                table[1][table[0].index(data[i][j])] += 1
    table = [[table[0][i], table[1][i]] for i in range(0, len(table[1]))]
    table = insertion_sort(table)
    return table

def insertion_sort(table):
    for j in range(1, len(table)):
        tmp = table[j]
        k = j - 1
        while k >= 0 and table[k][1] > tmp[1]:
            table[k + 1] = table[k]
            k -= 1
        table[k + 1] = tmp
    return table

def create_tree(table):
    mounting_tree = table[:]
    i = 0
    while True:
        left = mounting_tree[0][0]
        right = mounting_tree[1][0]
        freq = mounting_tree[0][1] + mounting_tree[1][1]
        no = tree(left, right)
        mounting_tree.append([no, freq])
        mounting_tree.remove(mounting_tree[0])
        mounting_tree.remove(mounting_tree[0])
        insertion_sort(mounting_tree)
        i += 1
        if len(mounting_tree) == 1:
            return mounting_tree

#Função criada com base no código do colega Gustavo Gino
#funcionamento da função totalmente compreendido
def create_huffman_table(tree, bit = ""):
    if isinstance(tree, str):
        return {tree: bit}
    table = dict()
    table.update(create_huffman_table(tree.left, bit + "0"))
    table.update(create_huffman_table(tree.right, bit + "1"))
    return table

def codify(data, table):
    encoded_text = ""
    for i in range(len(data)):
        for j in range(len(data[i])):
            encoded_text += table[data[i][j]]
    return encoded_text

def print_table(table, huffman):
    print("\nPrefix table:")
    for i in range(len(table)):
        print(" %5r | %5d | %15s" % (table[i][0], table[i][1], huffman[table[i][0]]))
    print("\n")

file_name = open(sys.argv[1], 'r')
print("File name: ", file_name)
file_data = file_name.readlines()
print("\nFila data: ", file_data)
file_size = size_file(file_data)
print("\nFile size: ", file_size)
alfabetic_table = frequency(file_data)
print("\nOrdered talble: ", alfabetic_table)
mounted_tree = create_tree(alfabetic_table)
#print("Tree: ", mounted_tree)
huffman_table = create_huffman_table(mounted_tree[0][0])
print("\nHuffman table: ", huffman_table)
encoded_text = codify(file_data, huffman_table)
print("\nEncoded : ", encoded_text)
print("\nEncoded size: ", len(encoded_text))
print("\nCompression efficiency: ", (len(encoded_text)/file_size)*100)
print_table(alfabetic_table, huffman_table)
