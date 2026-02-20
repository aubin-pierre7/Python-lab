#Creer et manipuler les variables de différents types de données
#Creation des variables
int_var = 19
float_var = 1.80
str_var = "Aubin"
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dict_var = {"nom": "Aubin", "role": "Etudiant"}
bool_var = True

#Affichage et manipulation des variables
print("Entier:", int_var)
print("Flottant:", float_var)
print("Chaîne de caractères:", str_var + " est un étudiant.")
list_var.append(4)
print("Liste après ajout d'un élément:", list_var)
print("Tuple:", tuple_var)
print("Dictionnaire:", dict_var["nom"])
print("Booléen:", bool_var)