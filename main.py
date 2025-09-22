"""Ce module contient des fonctions pour traiter les palindromes."""

import unicodedata # pour retirer les accents
import re  # pour les expressions régulières

#### Fonction secondaire


def retirer_accents(texte):
    """
    Retire les accents d'une chaîne de caractères.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', texte)
        if unicodedata.category(c) != 'Mn'
    )

def ispalindrome(p):
    """
    Indique si la chaîne de caractères p est un palindrome.
    Un palindrome est une chaîne qui se lit de la même façon de gauche à droite et de
    droite à gauche.
    On ne tient pas compte des espaces, de la casse et des accents."""
    p = retirer_accents(p) # enlever les accents
    p = p.lower() # mettre en minuscule
    p = re.sub(r'[^a-zA-Z0-9]', '', p)  # enlever les caractères spéciaux ainsi que les espaces
    print(p)
    print(p[::-1])

    return p == p[::-1]


#### Fonction principale

def main():
    """Fonction principale"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "deifie", "Émile-Éric, notre valet, alla te laver ton ciré élimé"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
