#Creer une fonction pour calculer et imprimer le factorielle d'un nombre
def factorielle(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)
    
def imprimer_factorielle(n):
    resultat = factorielle(n)
    print(f"La factorielle de {n} est: {resultat}")  
    
imprimer_factorielle(5)          