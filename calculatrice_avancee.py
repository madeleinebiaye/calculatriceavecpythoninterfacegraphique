memoire = 0

def calculer(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            print("Erreur : division par zéro !")
            return None
        return a / b
    else:
        print("Opérateur invalide !")
        return None


def calculatrice():
    global memoire
    resultat = 0

    print("\n" + "=" * 44)
    print("        CALCULATRICE AVANCEE")
    print("=" * 44)
    print("+  = Addition")
    print("-  = Soustraction")
    print("*  = Multiplication")
    print("/  = Division")
    print("M+ = Ajouter le resultat a la memoire")
    print("M- = Soustraire le resultat de la memoire")
    print("MR = Lire la memoire")
    print("MC = Effacer la memoire")
    print("Q  = Quitter")
    print("=" * 44)

    while True:
        print("\n" + "-" * 44)
        print(f"Resultat courant : {resultat}")
        print(f"Memoire          : {memoire}")
        print("-" * 44)

        choix = input("Commande (+, -, *, /, M+, M-, MR, MC, Q) : ").strip().upper()

        if choix in {"+", "-", "*", "/"}:
            try:
                a = float(input("Nombre 1 : "))
                b = float(input("Nombre 2 : "))

                res = calculer(a, choix, b)
                if res is not None:
                    resultat = res
                    print(f"=> Resultat : {resultat}")

            except ValueError:
                print("Erreur : entree invalide !")

        elif choix == "M+":
            memoire += resultat
            print(f"=> Memoire mise a jour : {memoire}")

        elif choix == "M-":
            memoire -= resultat
            print(f"=> Memoire mise a jour : {memoire}")

        elif choix == "MR":
            print(f"=> Valeur memoire : {memoire}")

        elif choix == "MC":
            memoire = 0
            print("=> Memoire reinitialisee.")

        elif choix == "Q":
            print("\nMerci d'avoir utilise la calculatrice. A bientot !")
            break

        else:
            print("Erreur : commande invalide.")


if __name__ == "__main__":
    calculatrice()