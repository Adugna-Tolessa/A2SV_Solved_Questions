def int_input():
    return int(input())

def map_input():
    return map(int, input().split())

def list_input():
    return list(map(int, input().split()))

def string_input():
    return input()

def list_of_strings():
    return input().split()

matrix = []
for _ in range(5):
    matrix.append(list_input())

count = 0
for i in range(5):
    if 1 in matrix[i] and i != 2:
        count += abs(i - 2)
        matrix[i], matrix[2] = matrix[2], matrix[i]
for col in range(5):
    if matrix[2][col] == 1:
        count += abs(col - 2)
print(count)

    
    

