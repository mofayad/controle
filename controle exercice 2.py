def PRIX(M):
    Tab = []
    prix_1 = 200 
    if M > 120 :
        prix_2 = 100 + (M - 120) * 0.5
    else:
        prix_2 = 100
    if M > 60 :
        prix_3 = 50 + (M - 60) * 1
    else:
        prix_3 = 50
    if M > 30 :
        prix_4 = 20 + (M - 30)* 1.5
    else:
        prix_4 = 20
    if M == 0 :
        prix_5 = M * 2
    
    Tab.append(prix_1)
    Tab.append(prix_2)
    Tab.append(prix_3)
    Tab.append(prix_4)
    Tab.append(prix_5)
    
    return Tab

while True:
        print("Menu :")
        print("1- Saisir la durée de communication: ")
        print("2- Afficher la liste du coût mensuel par offre: ")
        print("3- Afficher l'offre la plus intéressante (moindre coût): ")
        print("4- Quitter le programme")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            M = int(input("Entrer la durée de communication en minutes: "))

        elif choix == "2":
            prix_total = PRIX(M)
            print("Le coût mensuel par offre:")
            for i in range(prix_total):
                print(f"Abonnement {i + 1}:{prix_total[i]} DH")

        elif choix == "3":
            prix_total = PRIX(M)
            prix_min = min(prix_total)
            bon_abonnement = prix_total.index(prix_min) + 1
            print(f"L'offre la plus intéressante (moindre coût) est {bon_abonnement} qui coût {prix_min} DH")
        
        elif choix == "4":
            print("Fin du programme")
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide.")