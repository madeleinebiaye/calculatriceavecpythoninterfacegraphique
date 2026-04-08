from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno, showerror, showinfo

class MoteurCalculatrice:
    def __init__(self):
        self.premier_nombre = ""
        self.operateur = ""
        self.deuxieme_nombre = ""

    def afficher(self):
        return f"{self.premier_nombre}{self.operateur}{self.deuxieme_nombre}"

    def ajouter_chiffre(self, valeur):
        if self.operateur == "":
            self.premier_nombre += str(valeur)
        else:
            self.deuxieme_nombre += str(valeur)
        return self.afficher()

    def ajouter_operateur(self, valeur):
        if self.premier_nombre == "":
            return self.afficher()

        if self.deuxieme_nombre != "":
            return self.afficher()

        self.operateur = valeur
        return self.afficher()

    def effacer(self):
        self.premier_nombre = ""
        self.operateur = ""
        self.deuxieme_nombre = ""
        return self.afficher()

    def calculer(self):
        if self.premier_nombre == "" or self.operateur == "" or self.deuxieme_nombre == "":
            return self.afficher()

        try:
            nombre1 = float(self.premier_nombre)
            nombre2 = float(self.deuxieme_nombre)

            if self.operateur == "+":
                resultat = nombre1 + nombre2
            elif self.operateur == "-":
                resultat = nombre1 - nombre2
            elif self.operateur == "*":
                resultat = nombre1 * nombre2
            else:
                resultat = nombre1 / nombre2

            if resultat == int(resultat):
                self.premier_nombre = str(int(resultat))
            else:
                self.premier_nombre = str(resultat)

            self.operateur = ""
            self.deuxieme_nombre = ""
        except Exception:
            self.premier_nombre = ""
            self.operateur = ""
            self.deuxieme_nombre = ""
            return "Erreur"
        return self.afficher()


class MaFenetre:
    def __init__(self):
        self.moteur = MoteurCalculatrice()
        self.fenetre = Tk()
        self.fenetre.title("Calculatrice")
        self.fenetre.geometry("320x420")
        self.fenetre.minsize(300, 380)
        self.fenetre.rowconfigure(1, weight=1)
        self.fenetre.columnconfigure(0, weight=1)

        menubar = Menu(self.fenetre)
        self.fenetre.config(menu=menubar)

        menu_fichier = Menu(menubar, tearoff=0)
        menu_fichier.add_command(label="Enregistrer", command=self.sauvegarder)
        menu_fichier.add_command(label="Ouvrir...", command=self.ouvrir_fichier)
        menu_fichier.add_separator()
        menu_fichier.add_command(label="Quitter", command=self.quitter)
        menubar.add_cascade(label="Fichier", menu=menu_fichier)

        self.fenetre.bind_all("<Control-s>", lambda event: self.sauvegarder())

        menu_aide = Menu(menubar, tearoff=0)
        menu_aide.add_command(label="Tester pop-up", command=self.tester_popup)
        menu_aide.add_command(label="A propos", command=self.a_propos)
        menubar.add_cascade(label="Aide", menu=menu_aide)

        menu_salutation = Menu(menubar, tearoff=0)
        menu_salutation.add_command(
            label="Bonjour", command=lambda: showinfo("Bonjour", "Bonjour")
        )
        menu_salutation.add_separator()
        menu_salutation.add_command(
            label="Au revoir", command=lambda: self.fenetre.destroy()
        )
        menubar.add_cascade(label="Salutation", menu=menu_salutation)

        cadre_affichage = Frame(self.fenetre, padx=5, pady=5)
        cadre_affichage.grid(row=0, column=0, sticky="NSEW")
        cadre_affichage.columnconfigure(0, weight=1)

        cadre_boutons = Frame(self.fenetre, padx=5, pady=5)
        cadre_boutons.grid(row=1, column=0, sticky="NSEW")

        self.label = Label(
            cadre_affichage,
            text="",
            font=("Courier", 24, "bold"),
            anchor=E,
            bg="white",
            padx=10,
            pady=10
        )
        self.label.grid(row=0, column=0, sticky="NSEW")

        boutons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("=", 4, 1), ("C", 4, 2), ("+", 4, 3),
        ]

        operateurs = "+-*/"

        for texte, ligne, colonne in boutons:
            if texte.isdigit():
                commande = lambda valeur=texte: self.addDigit(valeur)
            elif texte in operateurs:
                commande = lambda valeur=texte: self.addOperator(valeur)
            elif texte == "=":
                commande = self.calculate
            else:
                commande = self.clear

            Button(
                cadre_boutons,
                text=texte,
                command=commande,
                height=2,
                width=4,
                bg="#567",
                fg="White",
                borderwidth=0,
                font=("Courier", 18, "bold")
            ).grid(row=ligne, column=colonne, padx=5, pady=5, sticky="NSEW")

        for index in range(4):
            cadre_boutons.columnconfigure(index, weight=1)

        for index in range(1, 5):
            cadre_boutons.rowconfigure(index, weight=1)

        self.fenetre.mainloop()

    def addDigit(self, valeur):
        self.label.config(text=self.moteur.ajouter_chiffre(valeur))

    def addOperator(self, valeur):
        self.label.config(text=self.moteur.ajouter_operateur(valeur))

    def calculate(self):
        self.label.config(text=self.moteur.calculer())

    def clear(self):
        self.label.config(text=self.moteur.effacer())

    def a_propos(self):
        showinfo("A propos", "Calculatrice Tkinter\nVersion 1.0")

    def tester_popup(self):
        if askyesno("Titre 1", "Cliquez sur oui"):
            showinfo("Titre 2", "Bravo !")
        else:
            showerror("Titre 4", ":(")

    def ouvrir_fichier(self):
        filename = askopenfilename()
        print(filename)
        if filename:
            showinfo("Fichier selectionne", filename)

    def sauvegarder(self):
        filename = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        if not filename:
            return

        try:
            with open(filename, "w", encoding="utf-8") as fichier:
                fichier.write(self.label.cget("text"))
            showinfo("Enregistrement", "Sauvegarde reussie")
        except Exception as erreur:
            showerror("Erreur", f"Impossible de sauvegarder : {erreur}")

    def quitter(self):
        if askyesno("Quitter", "Voulez-vous quitter l'application ?"):
            self.fenetre.destroy()

MaFenetre()