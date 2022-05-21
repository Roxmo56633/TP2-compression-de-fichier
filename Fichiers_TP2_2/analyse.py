"""
Module contenant une fonction permettant d'analyser la compression et la décompression
"""

from interaction_fichiers_texte import lire_fichier_brut
from os.path import isfile


def analyser(fichier_original, fichier_compresse, fichier_decompresse):
    """
    Cette fonction compare la taille du fichier compressé avec le fichier original et
    vérifie que le contenu du fichier décompressé est identique à celui du fichier original.

    Args:
        fichier_original (str): Le nom du fichier avant la compression
        fichier_compresse (str): Le nom fichier suivant la compression
        fichier_decompresse (str): Le nom du fichier suivant la décompression

    """

    texte_original = lire_fichier_brut(fichier_original)

    if not isfile(fichier_compresse):
        print("La compression n'a pas encore eu lieu!")
        return

    texte_compresse = lire_fichier_brut(fichier_compresse)

    print("Analyse de la compression...")
    print("Longueur du texte original: {}".format(len(texte_original)))
    print("Longueur du texte compressé: {}".format(len(texte_compresse)))
    print("La longueur du texte compressé est {:.0%} de la longueur originale.".format(
        len(texte_compresse) / len(texte_original)))

    if not isfile(fichier_decompresse):
        print("La décompression n'a pas encore eu lieu!")
        return

    texte_decompresse = lire_fichier_brut(fichier_decompresse)

    print("\nAnalyse de la décompression...")
    if texte_original == texte_decompresse:
        print("La décompression permet bien de retrouver le fichier original. ")
    else:
        print("ERREUR! La décompression est incohérente avec la compression. ")
