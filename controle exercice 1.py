def sousTableau(tableau, debut, fin):
    if debut <= fin :
        return tableau[debut:fin-1]
    else:
        return tableau[fin:debut-1]
while True:
    tableau = []
    for i in range(10):
        valeur = int(input(f"Entrer la valeur du case {i+1}:"))
        tableau.append(valeur)
    
    debut = int(input("Entrer le premier index:"))
    fin = int(input("Entrer le deuxieme index:"))

    resultat = sousTableau(tableau, debut, fin)
    print("Le sousTableau est:", resultat)

    continuer = input("Est-ce que vous souhaitez saisir une nouvelle liste ? (O/N): ")
    if continuer != "O" :
        break