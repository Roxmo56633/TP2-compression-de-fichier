"""
Fichier principal (point d'entrée du programme).
"""

from analyse import analyser
from compression import compresser
from decompression import decompresser

#ORIGINAL = 'fichiers_texte/poeme.txt'
#ORIGINAL = 'fichiers_texte/trop_court.txt'
ORIGINAL = 'fichiers_texte/lalala.txt'
COMPRESSE = 'fichiers_texte/compresse.txt'
DECOMPRESSE = 'fichiers_texte/decompresse.txt'


def selectionner_mode():
    """
    Dans cette fonction, on demande à l'utilisateur d'entrer le mode d'utilisation
    du programme voulu. Les options sont c pour compresser le fichier ORIGINAL en le fichier
    COMPRESSE, d pour décompresser le fichier COMPRESSE en le fichier DECOMPRESSE, a
    pour analyser l'efficacité de la compression et l'exactitude de la décompression, ou
    q pour quitter le programme. Dans le cas d'une option hors de ces quatre lettres, on affiche
    un message d'erreur et on redemande le mode.

    """

    mode = ''
    while mode != 'q':
        mode = input("Compresser (c), décompresser (d), analyser (a) ou quitter (q) ? ")
        print()
        if mode == 'c':
            compresser(ORIGINAL, COMPRESSE)
        elif mode == 'd':
            decompresser(COMPRESSE, DECOMPRESSE)
        elif mode == 'a':
            analyser(ORIGINAL, COMPRESSE, DECOMPRESSE)
        elif mode == 'q':
            print("Bonne fin de journée! ")
        else:
            print("Entrée non-valide. Veuillez entrer c, d, a ou q. ")
        print()


if __name__ == '__main__':
    selectionner_mode()
