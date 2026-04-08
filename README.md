# Calculatrice avec Interface Graphique Python

Calculatrice réalisée avec le module **Tkinter** de Python dans le cadre du cours **INF2032 – Python pour l'ingénieur**. Le projet propose une interface graphique interactive avec un moteur de calcul séparé, un système de menus, des fenêtres pop-up et la gestion de fichiers.

---

## 👩‍💻 Auteur

| Nom | Rôle |
|-----|------|
| **madeleinebiaye** | Développement complet – Interface Tkinter, moteur de calcul, menus, gestion fichiers |

---

## 🔍 Structure du projet

```
calculatrice/
├── calculatrice_base.py      # Interface graphique Tkinter + moteur de calcul
├── calculatrice_avancee.py   # Version avancee Tkinter (memoire M+, M-, MR, MC)
└── README.md                 # Documentation (ce fichier)
```

---

## ✅ Installation

Aucune installation de bibliothèque externe nécessaire. Tkinter est inclus dans Python par défaut.

```bash
# Vérifier que Python est installé
python --version

# Lancer la calculatrice graphique
python calculatrice_base.py

# Lancer la version avancee (memoire)
python calculatrice_avancee.py
```

---

## 🧩 Fonctionnalités

### Interface graphique (`calculatrice_base.py`)

- **Moteur de calcul** (`MoteurCalculatrice`) séparé de la vue
- **Interface Tkinter** (`MaFenetre`) construite avec `grid` et des `Frame`
- Fenêtre **responsive** (redimensionnable)
- Grille de boutons 4×4 : `7 8 9 /`, `4 5 6 *`, `1 2 3 -`, `0 = C +`
- Callbacks via **fonctions lambda** (`addDigit`, `addOperator`, `calculate`, `clear`)
- **Barre de menus** :
  - `Fichier` : Enregistrer, Ouvrir..., Quitter
  - `Aide` : Tester pop-up, A propos
  - `Salutation` : Bonjour, Au revoir
- **Raccourci clavier** : `Ctrl+S` pour sauvegarder
- **Pop-ups** : `showinfo`, `showerror`, `askyesno` via `tkinter.messagebox`
- **Sélecteur de fichiers** via `tkinter.filedialog`

### Calculatrice avancee (`calculatrice_avancee.py`)

- Addition, soustraction, multiplication, division
- Gestion de la **mémoire** (M+, M-, MR, MC) avec une ligne de boutons dediee
- `M+` en mode memoire : exemple `10` puis `M+` puis `2` donne `12`
- `M-` en mode memoire : exemple `10` puis `M-` puis `2` donne `8`
- `MR` rappelle la memoire comme resultat courant
- `MC` remet la memoire a `0` et efface la saisie (comme `C`)
- Menu `Aide` incluant une explication de chaque bouton
- Protection contre la **division par zéro**

---

## 🧠 Architecture

Le projet suit le principe **Modèle / Vue** :

```
MoteurCalculatrice        →  Gère les données (nombres, opérateur, calcul)
MaFenetre                 →  Gère l'affichage et les interactions
```

Les callbacks sont définis comme méthodes de la classe `MaFenetre` et appelés via des fonctions **lambda** :

```python
Button(..., command=lambda valeur=texte: self.addDigit(valeur))
```

---

## 📐 Concepts Tkinter utilisés

| Concept | Utilisation |
|---------|-------------|
| `Label` | Affichage du résultat |
| `Button` | Boutons de la calculatrice |
| `Frame` | Découpage de la fenêtre en zones |
| `grid` | Organisation en grille |
| `pack` | Placement avec marges |
| `Menu` | Barre de menus déroulants |
| `messagebox` | Fenêtres pop-up |
| `filedialog` | Sélection et sauvegarde de fichiers |
| `bind_all` | Raccourcis clavier (`Ctrl+S`) |
| `StringVar` | Variable liée à un champ texte |

---

## 🌟 Exemple d'usage

1. Lancer l'application :
```bash
python calculatrice_base.py
```

2. Effectuer un calcul :
   - Appuyer sur `1`, `2`, `+`, `8`, `=` → Résultat : `20`

3. Sauvegarder le résultat :
   - `Fichier > Enregistrer` ou `Ctrl+S`

4. Ouvrir un fichier :
   - `Fichier > Ouvrir...` → le chemin s'affiche dans la console

---

## 📚 Ressources

- [Documentation Tkinter](https://docs.python.org/3/library/tkinter.html)
- [tkinter.messagebox](https://docs.python.org/3/library/tkinter.messagebox.html)
- [tkinter.filedialog](https://docs.python.org/3/library/dialog.html)

---

## ⚠️ Notes

- Tkinter est intégré à Python, aucun `pip install` n'est nécessaire.
- La calculatrice effectue **une seule opération à la fois** (pas de succession d'opérations enchaînées).
- En cas d'erreur (ex : division par zéro), appuyer sur `C` pour réinitialiser.

---

*Projet réalisé dans le cadre du cours INF2032 – Python pour l'ingénieur – ESMT*