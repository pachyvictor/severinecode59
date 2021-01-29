def tableau_to_texte(tableau):
    """ Cette fonction transforme un tableau en
    une chaîne lisible et printable"""

    chaine = str()
    for ligne in tableau:
        chaine += " ".join(ligne)
        chaine += "\n"

    return chaine
