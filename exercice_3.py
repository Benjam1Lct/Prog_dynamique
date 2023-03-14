def chemin(n, m):
    matrice = [[1 for j in range(m)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            matrice[i][j] = matrice[i-1][j] + matrice[i][j-1]

    return matrice[n-1][m-1]

print(chemin(10, 10))