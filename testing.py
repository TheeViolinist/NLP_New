matriz = [[1,2,3], [1.5, 5, 9.2], [0.2, 1.8, 0.1], [1,0.01, 2]]


indiceMenor = 0
indiceMenor2 = 0
menor = matriz[0][0]
maior = matriz[0][0]
indiceMaior1 = 0
indiceMaior2 = 0

print(matriz[0])

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            indiceMenor = i
            indiceMenor2 = j
        
        if matriz[i][j] > maior and i != j:
            maior = matriz[i][j]
            indiceMaior1 = i
            indiceMaior2 = j
    
        

print(matriz[indiceMaior1][indiceMaior2])
print(matriz[indiceMenor][indiceMenor2])