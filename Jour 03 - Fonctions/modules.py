#Nous pouvons importer des modules entiers
import math
resultat = math.sqrt(16)
print("La racine carrée de 16 est:", resultat)

#Nous pouvons aussi importer des fonctions spécifiques d'un module
from math import sqrt
resultat = sqrt(16)
print("La racine carrée de 16 est:", resultat)

#Nous pouvons aussi importer un module entier avec un alias
import math as m
resultat = m.sqrt(16)
print("La racine carrée de 16 est:", resultat)

#Nous pouvons aussi creer nos propres modules en créant un fichier .py et en y mettant des fonctions ou des variables (A voir plutard)