import unicodedata
import string
import math
from functools import reduce


alphabet = string.ascii_uppercase
TAILLE_ALPHABET = len(alphabet)

def normaliseTexte(texte: str) -> str:
    # Cette fonction prend en entré un texte au format str et retourne un texte normalisé de type str
    # Le texte normalisé est en majuscule, sans accents et sans caractères spéciaux

    texte = texte.upper()
    texte = unicodedata.normalize('NFD', texte)
    for lettre in texte:
        if lettre not in alphabet:
            texte = texte.replace(lettre, '')
    return texte

def chiffreVigenere( texte :str , cle : str) -> str:
    # Cette fonction prend en entrée un texte de type str et une clé de chiffrement de type str 
    # Elle retourne ensuite un texte chiffré de type str

    resultat : str = ""
    texte = normaliseTexte(texte)
    cle = normaliseTexte(cle)
    longueurCLe = len(cle)
    
    for element in range(len(texte)):
        resultat += alphabet[(alphabet.index(texte[element]) + alphabet.index(cle[element % longueurCLe])) % TAILLE_ALPHABET]
    return resultat

def dechiffreVigenere( texte :str, cle : str) -> str :
    # Cette fonction prend en entrée un texte de type str et une clé de déchiffrement de type str
    # Elle retourne ensuite un texte déchiffré de type str

    resultat : str = ""
    texte = normaliseTexte(texte)
    cle = normaliseTexte(cle)
    longueurCLe = len(cle)
    
    for element in range(len(texte)):
        resultat += alphabet[(alphabet.index(texte[element]) - alphabet.index(cle[element % longueurCLe])) % TAILLE_ALPHABET]
    return resultat   

def trouverRepetitions(texte) -> dict:
    # Cette fonction prend en entrée un texte de type str
    # Elle retourne un dictionnaire contenant les répétitions de sous-chaînes de longueur 3 et 4

    TAILLE_REPETITION = [3,4]
    repet : dict = {}
    
    for longueur in TAILLE_REPETITION:
        for i in range(len(texte) - longueur):
            sous_chaine = texte[i:i + longueur]
            positions = []
            
            for j in range(i + longueur, len(texte) - longueur + 1):
                if texte[j:j + longueur] == sous_chaine:
                    positions.append(j)
            
            if positions:
                if sous_chaine in repet:
                    repet[sous_chaine].extend([pos - i for pos in positions])
                else:
                    repet[sous_chaine] = [pos - i for pos in positions]
    return repet

def pgcd(distances : list[int]) -> int:
    # Cette fonction prend en entrée une liste de distances de type list[int]
    # Elle retourne le plus grand diviseur commun de ces distances

    return reduce(math.gcd, distances)

def changeDicoEnListe(dico : dict) -> list:
    # Cette fonction prend en entrée un dictionnaire de type dict
    # Elle retourne une liste contenant les valeurs du dictionnaire

    return [valeur for sous_liste in dico.values() for valeur in sous_liste]

def compteDiviseurOccurence(listeRepet: list[int]) -> dict[int, int]:
    # Cette fonction prend en entrée une liste de répétitions de type list[int]
    # Elle retourne un dictionnaire contenant les diviseurs et leur occurence

    candidats : dict[int, int] = {}

    for nombre in listeRepet:
        for diviseur in range(2, nombre // 2 + 1):  
            if nombre % diviseur == 0:
                if diviseur not in candidats:
                    candidats[diviseur] = 1
                else:
                    candidats[diviseur] += 1
    return candidats

def trierOccurenceDiviseursDesc(candidats : dict[int, int]) -> dict[int, int]:
    # Cette fonction prend en entrée un dictionnaire de type dict[int, int]
    # Elle retourne un dictionnaire trié par ordre décroissant des occurences

    return dict(sorted(candidats.items(), key=lambda x: x[1], reverse=True))

def methodeKasiski(chemin_fichier : str) -> None:
    # Cette fonction prend en entrée un chemin de fichier de type str
    # Elle affiche les 5 clés potentielles les plus probables

    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            fichier.close()
            contenu = normaliseTexte(contenu)

            repet = trouverRepetitions(contenu)
            if repet == {}:
                print("???")
            else:
                listeCandidats = changeDicoEnListe(repet)
                candidats = compteDiviseurOccurence(listeCandidats)
                candidats = trierOccurenceDiviseursDesc(candidats)
                for diviseur, occurence in list(candidats.items())[:5]:
                   print(f"Clé potentielle : {diviseur}, Occurrence du diviseur : {occurence}")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
