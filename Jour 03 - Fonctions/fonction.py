#Creer une fonction avec des parametres et valeur de retour
def addition(a, b):
    return a + b
resultat = addition(5, 3)
print("Le resultat de l'addition est:", resultat)


#Nous avons les variables a portees locales et des variables a portees globales
#Portee locale

def salutation():
    message = "Bonjour"  # variable locale
    print(message)
salutation()
#print(message)  # Cela va provoquer une erreur car 'message' est une variable locale et n'est pas accessible en dehors de la fonction


#Portee globale
salutation = "Bonjour"  # variable globale
def dire_bonjour():
    print(salutation + "Depuis l'interieur de la fonction")  # Accès à la variable globale 

dire_bonjour()
print(salutation + "Depuis l'exterieur de la fonction")  # Accès à la variable globale en dehors de la fonction    