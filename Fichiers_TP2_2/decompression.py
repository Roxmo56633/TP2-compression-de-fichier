"""
Module contenant les fonctions permettant d'effectuer la décompression
"""

from compression import SYMBOLES
from interaction_fichiers_texte import lire_fichier_compresse, ecrire_fichier_decompresse


def remplacer_symbole_par_paire(chaine, paire, symbole):
    """
    Cette fonction remplace toutes les occurences du symbole par la paire en argument.

    Exemple:
    chaine=haXhaXX, paire=hi, symbole=X
    Donc la fonction retournerait "hahihahihi"

    Args:
        chaine (str): La chaîne où effectuer des remplacements
        paire (str): La paire à mettre au lieu du symbole
        symbole (str): Le symbole à remplacer

    Returns:
        str: La chaîne suite aux remplacements

    """

    # Votre code ici


    # code
    liste_chaine = list(chaine)

    n = len(chaine)
    for i in range(len(liste_chaine[:n])):
        symbole_a_verifier = liste_chaine[i]

        if symbole == symbole_a_verifier:
            liste_chaine[i] = paire

    chaine_remplace = "".join(liste_chaine)  # transformer la liste en chaine, pour retourner une chaine de caractères
    return chaine_remplace

def decompression_par_paires(chaine, dictionnaire_paires):
    """
        Cette fonction effectue toute la décompression sur la chaîne en argument,
        en utilisant le dictionnaire de paires.
        Parcourir chaque symbole (importez la variable globaleSYMBOLES du fichier compression)
        en ordre inverse, et remplacer toutes les occurences de ce symbole par la paire correspondante.
        N'oubliez pas de réutiliser la fonction programmée ci-haut.

        Args:
            chaine (str): La chaîne compressée.
            dictionnaire_paires (dict): Le dictionnaire de paires.

        Returns:
            str: La chaîne décompressée.

        """
    for symbole in SYMBOLES[::-1]: #DONNE UNE LISTE À L'ENVERS!
        if symbole in dictionnaire_paires:
            paire = dictionnaire_paires[symbole]
            chaine = remplacer_symbole_par_paire(chaine, paire, symbole)
    return chaine


def decompresser(fichier_compresse, fichier_decompresse):
    """
    Cette fonction lit le fichier compressé, le décompresse et écrit le résultat
    dans le fichier décompressé.

    Note: cette fonction devrait principalement appeler d'autres fonctions

    Args:
        fichier_compresse (str): Le nom du fichier où lire le contenu compressé
        fichier_decompresse (str): Le nom du fichier où écrire le contenu décompressé
    """

    print("Décompression en cours...")
    chaine_compresse, dictionnaire_paire = lire_fichier_compresse(fichier_compresse)
    chaine_decompresse = decompression_par_paires(chaine_compresse, dictionnaire_paire)
    ecrire_fichier_decompresse(fichier_decompresse, chaine_decompresse)
    print("Décompression complétée!")


if __name__ == '__main__':
    assert remplacer_symbole_par_paire("haXhaXX", "hi", "X") =="hahihahihi"
    assert decompression_par_paires("E", {"A": "hi", "B": "ha", "C": "BA", "D": "CC", "E": "DA"}) == "hahihahihi"
