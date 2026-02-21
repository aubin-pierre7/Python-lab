#Programme qui calcule le factoriel d'un nombre en utilisant une boucle while

nombre = int(input("Entrez le nombre dont vous voulez le factoriel: "))
resultat = 1
i=1
while i <= nombre:
    resultat *= i
    i += 1
print(f"le factoriel de {nombre} est {resultat}.")    