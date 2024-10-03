import unicodedata
import string
import math
from functools import reduce


alphabet = string.ascii_uppercase
TAILLE_ALPHABET = len(alphabet)

def normaliseTexte(texte: str) -> str:
    texte = texte.upper()
    texte = unicodedata.normalize('NFD', texte)
    for lettre in texte:
        if lettre not in alphabet:
            texte = texte.replace(lettre, '')


    return texte

def chiffre_vigenere( texte :str , cle : str) -> str:
    resultat : str = ""
    texte = normaliseTexte(texte)
    cle = normaliseTexte(cle)
    longueurCLe = len(cle)
    
    for element in range(len(texte)):
        resultat += alphabet[(alphabet.index(texte[element]) + alphabet.index(cle[element % longueurCLe])) % TAILLE_ALPHABET]

    return resultat

def dechiffre_vigenere( texte :str, cle : str) -> str :
    resultat : str = ""
    texte = normaliseTexte(texte)
    cle = normaliseTexte(cle)
    longueurCLe = len(cle)
    
    for element in range(len(texte)):
        resultat += alphabet[(alphabet.index(texte[element]) - alphabet.index(cle[element % longueurCLe])) % TAILLE_ALPHABET]

    return resultat   

def trouverRepetitions(texte) -> dict:

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
    return reduce(math.gcd, distances)

def changeDicoEnListe(dico : dict) -> list:
    return [valeur for sous_liste in dico.values() for valeur in sous_liste]

def compteDiviseurOccurence(listeRepet: list[int]) -> dict[int, int]:
    contacts : dict[int, int] = {}

    for nombre in listeRepet:
        for diviseur in range(2, nombre // 2 + 1):  
            if nombre % diviseur == 0:
                if diviseur not in contacts:
                    contacts[diviseur] = 1
                else:
                    contacts[diviseur] += 1

    return contacts

def methodeKasiski(chemin_fichier : str) -> None:
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            fichier.close()
            contenu = normaliseTexte(contenu)

            repet = trouverRepetitions(contenu)
            if repet == {}:
                print("???")
            else:
                listeContacts = changeDicoEnListe(repet)
                contacts = compteDiviseurOccurence(listeContacts)
                for diviseur, occurence in list(contacts.items())[:5]:
                   print(f"Clé potentielle : {diviseur}, Occurence du diviseur : {occurence}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

print("MENU :")
print("1. Chiffrer un message")
print("2. Déchiffrer un message")
print("3. Trouver la taille d'une clé dans un fichier")
print("4. Quitter")
choix = input()
if choix == "1":
    texte = input("Entrez le message à chiffrer : ")
    cle = input("Entrez la clé de chiffrement : ")
    print("Votre message chiffré : " + chiffre_vigenere(texte, cle))

elif choix == "2":
    texte = input("Entrez le message à déchiffrer : ")
    cle = input("Entrez la clé de déchiffrement : ")
    print("Votre message déchiffré : " + dechiffre_vigenere(texte, cle))

elif choix == "3":
    chemin_fichier = input("Entrez le chemin du fichier à lire : \n")
    kasiskiMethod(chemin_fichier)

elif choix == "4":
    print("Au revoir !")

else:
    print("Choix invalide")