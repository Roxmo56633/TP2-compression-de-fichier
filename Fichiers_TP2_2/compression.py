"""
Module contenant les fonctions permettant d'effectuer la compression
"""

from interaction_fichiers_texte import lire_fichier_brut, ecrire_fichier_compresse

SYMBOLES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def trouver_paire_la_plus_frequente(chaine):
    """
    Cette fonction trouve la paire de symboles subséquents la plus commune dans
    la chaîne de caractères en argument.

    Attention: Mis à part les symboles aux extrémités, chaque symbole fait partie de
    deux paires de symboles. Indice: dans une chaîne de n symboles, il y a n-1 paires.

    Exemple:
    hahihahihi -> ha: 2, ah: 2, hi: 3, ih: 2
    Donc la fonction retournerait "hi"

    Args:
        chaine (str): La chaîne de caractère à analyser

    Returns:
        str: La paire de symboles la plus fréquente dans chaine

    """
    liste_paire = []
    n = len(chaine)
    for i in range((len(chaine[:n - 1]))):
        paire = chaine[i:i+2]
        liste_paire.append(paire)

    # # compter le nombre de fois que chaque paires se répettent
    compteur_paire = {}
    for paire in liste_paire:
        if paire in compteur_paire:
            compteur_paire[paire] += 1
        else:
            compteur_paire[paire] = 1

    # sortir la ou les paires avec le plus d'ittération
    compte_plus_gros = 0
    for valeur_compteur in compteur_paire.values():
        if valeur_compteur > compte_plus_gros:
            compte_plus_gros = valeur_compteur

    #utiliser compte_le_plus_gros pour trouver une ou des clé de dictionnaire --> liste en prévision si plus qu'une clé obtenue:
    liste_paire_frequente = []
    for paire, compte_paire in compteur_paire.items():
        if compte_paire == compte_plus_gros:
            liste_paire_frequente.append(paire)

    #trouver la première paire la plus fréquence s'il y en as plusieurs à la même fréquence
    compte_paire2 = 0
    if len(liste_paire_frequente) == 1:
        return "".join(liste_paire_frequente[0])
    else:
        for paire in liste_paire_frequente:
            if paire in liste_paire and compte_paire2 == 0:
                compte_paire2 += 1
                return "".join(paire)


def remplacer_paire_par_symbole(chaine, paire, symbole):
    """
    Cette fonction remplace toutes les occurences de la paire dans la chaine
    par le symbole.

    Exemple:
    chaine=hahihahihi, paire=hi, symbole=X
    Donc la fonction retournerait "haXhaXX"

    Args:
        chaine (str): La chaîne où effectuer des remplacements
        paire (str): La paire à remplacer
        symbole (str): Le symbole à mettre au lieu de la paire

    Returns:
        str: La chaîne suite aux remplacements

    """
    # code
    liste_chaine = list(chaine)
    liste_paire = list(paire)

    n = len(chaine)
    for i in range(len(chaine[:n-1])):
        print(i)
        paire_a_verifier = liste_chaine[i:i + 2]

        if liste_paire == paire_a_verifier:
            liste_chaine[i:i+2] = symbole


    chaine_remplace = "".join(liste_chaine)  # transformer la liste en chaine, pour retourner une chaine de caractères
    return chaine_remplace


def afficher_progression(ratio):
    """
    Cette fonction affiche une barre de progression correspondant à la fraction
    reçue en argument.

    Args:
        ratio (float): La fraction de progression, entre 0 et 1.
    """

    print("\rProgression: [{0:50s}] {1:.1f}%".format('#' * int(ratio * 50), ratio * 100),
          end="", flush=True)


def compression_par_paires(chaine):
    """
    Cette fonction effectue toute la compression sur la chaîne en argument.
    Pour chaque symbole (voir la variable globale symboles), on
    trouve la paire la plus fréquente, on l'ajoute à un dictionnaire associant le symbole
    avec la paire, et on remplace la paire par le symbole dans la chaîne.
    La fonction doit arrêter s'il n'y a plus de symboles disponibles OU si la chaîne ne contient plus
    qu'un seul symbole.
    N'oubliez pas de réutiliser les fonctions programmées ci-haut.

    Facultatif: affichez la progression à chaque itération en appelant la fonction afficher_progression.

    Args:
        chaine (str): La chaîne à compresser.

    Returns:
        str: La chaîne compressée
        dict: Le dictionnaire de paires.

    """
    dict_symboles = {}
    for i in range(len(SYMBOLES)):
        if i < len(SYMBOLES) + 1 and len(chaine) > 1:
            symbole_remplacement = SYMBOLES[i]
            paire_plus_frequente = trouver_paire_la_plus_frequente(chaine)
            if symbole_remplacement not in dict_symboles.keys() and paire_plus_frequente not in dict_symboles.values():
                dict_symboles[symbole_remplacement] = paire_plus_frequente
                chaine = remplacer_paire_par_symbole(chaine, paire_plus_frequente, symbole_remplacement)
                print(chaine, dict_symboles)
    return chaine, dict_symboles


def compresser(fichier_original, fichier_compresse):
    """
    Cette fonction lit le fichier original, le compresse et écrit le résultat
    dans le fichier compressé.

    Note: cette fonction devrait principalement appeler d'autres fonctions

    Args:
        fichier_original (str): Le nom du fichier où lire le contenu original
        fichier_compresse (str): Le nom du fichier où écrire le contenu compressé
    """

   # ecrire_fichier_compresse(fichier_compresse, chaine_compresse, dict_symboles)
    print("Compression en cours...")
    chaine_original = lire_fichier_brut(fichier_original)
    chaine_compresse, dict_symbole = compression_par_paires(chaine_original)
    ecrire_fichier_compresse(fichier_compresse, chaine_compresse, dict_symbole)
    print("Compression complétée!")


if __name__ == '__main__':
    chaine_test = "hahihahihi"
    chaine_test2 = "salut les amis, tirez vous une buche!!!!!!!!!!!!!!!!"
    chaine_test3 = "12345654321667766336688662266"
    chaine_test4 = "AAB"
    assert trouver_paire_la_plus_frequente(chaine_test) == "hi"
    assert trouver_paire_la_plus_frequente(chaine_test2) == "!!"
    assert trouver_paire_la_plus_frequente(chaine_test3) == "66"
    assert trouver_paire_la_plus_frequente(chaine_test4) == "AA"
    assert remplacer_paire_par_symbole(chaine_test, "hi", "X") == "haXhaXX"
    assert compression_par_paires(chaine_test) == \
           ("E", {"A": "hi", "B": "ha", "C": "BA", "D": "CC", "E": "DA"})
