def sac_a_dos_dyna(masse, valeur, indice):
    K = [[0 for x in range(indice + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(masse + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(valeur[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
        
    return K[len(valeur)][masse]


Masse = [1,2,3,4,5,6]
Valeur = [10,32,42,18,85,114]
sac_a_dos_dyna(Masse, Valeur, 10)