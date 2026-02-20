                         # LES INSTRUCTIONS CONDITIONNELLES
#Exemple 1
nombre = 10 
if nombre > 0:
    print("Le nombre est positif.")
elif nombre == 0:
    print("Le nombre est zéro.")
else:
    print("Le nombre est négatif.")
    

# #Exmple 2: Condition imbriquée
age = 25
if age > 18:
    if age < 30:
        print("Vous etes un jeune adulte.")
    else:
        print("Vous etes un adulte.")   
        
        
        
             
                         # LES BOUCLES
# I - Boucle for
#Exemple 1:
Fruits = ["Banane", "Orange", "Mangue"]
for fruit in Fruits:
    print(fruit)
   
#Exemple 2: Utilisation de la fonction range()
for i in range(5):
    print(i)
    
    
# II - Boucle while
#Exemple 1:
count = 0
while count < 5:
    print(count)
    count += 1
print("Boucle terminée.")                                

#Ne pas oublier break et continue
#Exemple 1: Utilisation de break
for i in range(10):
    if i == 5:
        break
    print(i) 

#Exemple 2: Utilisation de continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)    