"""
Module contenant les fonctions permettant d'interagir avec des fichiers texte
"""

SEPARATEUR_CLE_VALEUR = ":"
SEPARATEUR_ENTREES = "#"


def convertir_dictionnaire_en_chaine(dictionnaire_paires):
    """
    Cette fonction convertit un dictionnaire d tel que d["X"] = "yz" en une chaîne
    de caractère où chaque entrée est au format #X:yz, mises bout à bout

    Args:
        dictionnaire_paires (dict): Le dictionnaire de paires

    Returns:
        str: La chaîne de caractère représentant le dictionnaire

    """

    chaine_dictionnaire = ""
    for symbole in dictionnaire_paires.keys():
        chaine_dictionnaire += "{}{}{}{}".format(SEPARATEUR_ENTREES, symbole,
                                                 SEPARATEUR_CLE_VALEUR, dictionnaire_paires[symbole])
    return chaine_dictionnaire


def convertir_chaines_en_dictionnaire(liste_chaines_paires):
    """
    Cette fonction prend en entrée une liste de chaînes au format "#X:yz" et
    en fait un dictionnaire d tel que d["X"] = "yz"

    Args:
        liste_chaines_paires (list): La liste de chaînes de paires

    Returns:
        dict: Le dictionnaire associant les symboles de gauche aux paires

    """

    dictionnaire_paires = {}
    for entree in liste_chaines_paires:
        symbole, paire = entree.split(SEPARATEUR_CLE_VALEUR)
        dictionnaire_paires[symbole] = paire
    return dictionnaire_paires


def lire_fichier_brut(nom_fichier):
    """
    Cette fonction lit un fichier et en retourne son contenu.

    Args:
        nom_fichier (str): Le nom du fichier à lire

    Returns:
        str: Le contenu du fichier

    """

    with open(nom_fichier, 'r') as fichier:
        chaine = fichier.read()
    return chaine


def lire_fichier_compresse(nom_fichier):
    """
    Cette fonction lit un fichier compressé et interprète son contenu comme étant
    la chaîne compressée suivie du dictionnaire de paires.

    On utilise la fonctionnalité split dont voici un exemple:
    "abc$def$ghi".split("$")
    Cela donne la liste ["abc", "def", "ghi"]

    N'oubliez pas d'appeler la fonction convertir_chaines_en_dictionnaire.

    Args:
        nom_fichier (str): Le fichier à lire

    Returns:
        str: La chaîne compressée
        dict: Le dictionnaire de paires

    """

    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.read().split(SEPARATEUR_ENTREES)
        chaine_compressee = lignes[0]
        dictionnaire_paires = convertir_chaines_en_dictionnaire(lignes[1:])
    return chaine_compressee, dictionnaire_paires


def ecrire_fichier_compresse(nom_fichier, chaine_compressee, dictionnaire_paires):
    """
    Cette fonction écrit dans un fichier un texte compressé, c'est-à-dire la chaîne
    compressée suivi du dictionnaire de paires mis sous forme de chaîne
    de caractères.

    Args:
        nom_fichier (str): Le nom du fichier dans lequel écrire
        chaine_compressee (str): La chaîne compressée
        dictionnaire_paires (dict): Le dictionnaire de paires

    """

    chaine_dictionnaire = convertir_dictionnaire_en_chaine(dictionnaire_paires)
    with open(nom_fichier, 'w') as f:
        f.write(chaine_compressee + chaine_dictionnaire)


def ecrire_fichier_decompresse(nom_fichier, chaine):
    """
    Cette fonction écrit une chaîne de longueur arbitraire dans un fichier.

    Args:
        nom_fichier (str): Le nom du fichier dans lequel écrire
        chaine (str): La chaîne à écrire dans le fichier

    """

    with open(nom_fichier, 'w') as fichier:
        fichier.write(chaine)


if __name__ == '__main__':
    assert convertir_dictionnaire_en_chaine({"A": "hi", "B": "ha", "C": "BA", "D": "CC", "E": "DA"}) == \
           "#A:hi#B:ha#C:BA#D:CC#E:DA"
    assert convertir_chaines_en_dictionnaire(["A:hi", "B:ha", "C:BA", "D:CC", "E:DA"]) == \
           {"A": "hi", "B": "ha", "C": "BA", "D": "CC", "E": "DA"}
