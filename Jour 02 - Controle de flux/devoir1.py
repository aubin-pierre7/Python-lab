# Programme qui calcule le factoriel d'un nombre en utilisant une boucle while
nombre = int(input("Entrez un nombre : "))

resultat = 1      # Variable pour stocker le résultat final
i = 1             # Compteur qui part de 1

while i <= nombre:        # Tant que i n'a pas dépassé le nombre
    resultat *= i         # Multiplie le résultat par i
    i += 1                # Passe au nombre suivant

print(f"Le factoriel de {nombre} est {resultat}")