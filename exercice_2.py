def monnaie_dyn(valeur, systeme):
    Nb_min = [i for i in range(valeur + 1)]
    sol = [[]] * (valeur + 1)
   
    for v in range(1, valeur + 1):
        for pi in systeme:
            if pi <= v and Nb_min[v - pi] + 1 < Nb_min[v]:
                Nb_min[v] = Nb_min[v - pi] + 1
                sol[v] = sol[v - pi] + [pi]
               
    return Nb_min[valeur]

def monnaie_dyn_solution(valeur, systeme):
    Nb_min = [i for i in range(valeur + 1)]
    sol = [[]] * (valeur + 1)
   
    for v in range(1, valeur + 1):
        for pi in systeme:
            if pi <= v and Nb_min[v - pi] + 1 < Nb_min[v]:
                Nb_min[v] = Nb_min[v - pi] + 1
                sol[v] = sol[v - pi] + [pi]
               
    return sol[valeur]

if __name__ == "__main__":
    system = [1, 2, 5, 10]
    print(monnaie_dyn_solution(14, system))

#"Nb_min[v] = min(Nb_min[v - pi] + 1)" si <= pi