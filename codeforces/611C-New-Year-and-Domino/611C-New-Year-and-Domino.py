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


h, w = map_input()

matrix = []
for _ in range(h):
    s = string_input()
    matrix.append(s)

# prefix arrays
hor = [[0]*(h+1) for _ in range(w+1)]
ver = [[0]*(h+1) for _ in range(w+1)]

for y in range(h):
    for x in range(w):
        hor[x+1][y+1] = hor[x][y+1] + hor[x+1][y] - hor[x][y]
        ver[x+1][y+1] = ver[x][y+1] + ver[x+1][y] - ver[x][y]

        if matrix[y][x] != '.':
            continue

        if x != w-1 and matrix[y][x+1] == '.':
            hor[x+1][y+1] += 1

        if y != h-1 and matrix[y+1][x] == '.':
            ver[x+1][y+1] += 1


q = int_input()

for _ in range(q):
    y1, x1, y2, x2 = map_input()

    x1 -= 1
    y1 -= 1

    ans = 0

    ans += hor[x2-1][y2] - hor[x1][y2] - hor[x2-1][y1] + hor[x1][y1]
    ans += ver[x2][y2-1] - ver[x1][y2-1] - ver[x2][y1] + ver[x1][y1]

    print(ans)