l = []
matrix = []
g = int(input("enter puzzleno:"))
print("enter puzzle")
for i in range(0,5):
    l = list(raw_input())
    matrix.append(l)
x = []
p = []
m = ' '
print("enter operations")
for y in range(0,1):
    p = list(raw_input())
for j in range(0,5):
    for t in range(0,5):
        if matrix[j][t] == m:
            e = j
            c = t
ve = 0
for x2 in range(0,len(p)):
    for x1 in range(0,5):
        if matrix[x1][4] == ' ':
            if p[x2] == 'R':
                ve+=1
if ve>=1:
    print("this puzzle has no configuration")

else:
    for u in range(0,len(p)):
        if p[u] == 'A':
            temp = matrix[e][c]
            matrix[e][c] = matrix[e-1][c]
            matrix[e-1][c] = temp
            e = e - 1
        if p[u] == 'B':
            temp = matrix[e][c]
            matrix[e][c] = matrix[e+1][c]
            matrix[e+1][c] = temp
            e = e + 1
        if p[u] == 'R':
            temp = matrix[e][c]
            matrix[e][c] = matrix[e][c+1]
            matrix[e][c+1] = temp
            c = c + 1
        if p[u] == 'L':
            temp = matrix[e][c]
            matrix[e][c] = matrix[e][c-1]
            matrix[e][c-1] = temp
            c = c - 1
print("puzzle #:{}".format(g))
for f in range(0,5):
    z = matrix[f]
    s = ' '
    print(s.join(z))
