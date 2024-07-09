import random
mat = [0]*3
for i in range(3):
    mat[i] = [0]*3

for i in range(3):
    for j in range(3):
        mat[i][j] = random.randint(10,50)
print(mat)

maior = mat[1][0]
for i in range(3):
    for j in range(3):
        if i != j:
            if mat[i][j] > maior:
                maior = mat[i][j]
print(maior)    
            
