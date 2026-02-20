#Creation d'une calculatrce a menu simple
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Il est impossible de diviser un nombre  par zéro."
    
while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    
    choix = input("Choisissez une option (1-5): ")
    
    if choix == '5':
        print("Merci d'avoir utilisé la calculatrice. Au revoir!")
        break
    
    if choix in ['1', '2', '3', '4']:
        num1 = float(input("Entrez le premier nombre: "))
        num2 = float(input("Entrez le deuxième nombre: "))
        
        if choix == '1':
            result = addition(num1, num2)
            print(f"Résultat: {num1} + {num2} = {result}")
        elif choix == '2':
            result = soustraction(num1, num2)
            print(f"Résultat: {num1} - {num2} = {result}")
        elif choix == '3':
            result = multiplication(num1, num2)
            print(f"Résultat: {num1} * {num2} = {result}")
        elif choix == '4':
            result = division(num1, num2)
            print(f"Résultat: {num1} / {num2} = {result}")
    else:
        print("Option invalide. Veuillez choisir une option entre 1 et 5.")    