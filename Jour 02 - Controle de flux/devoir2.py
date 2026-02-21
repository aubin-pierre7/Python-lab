#Programme qui trouve le plus grand nombre dans une liste en utilisant une boucle for

liste = [5, 12, 7, 3, 9]

maxi = liste[0]          # On initialise le maximum avec le premier élément

for nombre in liste:      # Parcours de tous les éléments
    if nombre > maxi:     # Si on trouve un nombre plus grand
        maxi = nombre    # On met à jour le maximum

print(f"Le plus grand nombre de la liste est {maxi}")