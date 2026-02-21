# Ce programme utilise les fonctions définies dans le module operations_mathematiques pour effectuer des opérations mathématiques de base sur deux nombres entrés par l'utilisateur.
import operations_mathematiques as om

a = int(input("Entrez le premier nombre: "))
b = int(input("Entrez le deuxième nombre: "))

print(f"Addition de {a} et {b}: {om.addition(a, b)}")
print(f"Soustraction de {a} et {b}: {om.soustraction(a  , b)}")
print(f"Multiplication de {a} et {b}: {om.multiplication(a, b)}")
print(f"Division de {a} et {b}: {om.division(a, b)}")