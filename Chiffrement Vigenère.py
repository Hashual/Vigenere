import unicodedata
import string

alphabet = string.ascii_uppercase
TAILLE_ALPHABET = 26

def normalizeTexte(texte: str) -> str:

    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(c for c in texte if unicodedata.category(c) != 'Mn')
    texte = ''.join(c for c in texte if c in string.ascii_letters or c in string.digits)
    texte = texte.upper()

    return texte

def chiffre_vigenere( phrase :str , cle : str) -> str:
    resultat : str = ""

    phrase = normalizeTexte(phrase)

    cle = normalizeTexte(cle)

    longueurCLe = len(cle)
    
    for element in range(len(phrase)):
        if phrase[element] in alphabet:
            resultat += alphabet[(alphabet.index(phrase[element]) + alphabet.index(cle[element % longueurCLe])) % TAILLE_ALPHABET]
        else:
            resultat += phrase[element]
    return resultat

def dechiffre_vigenere( phrase :str, cle : str) -> str :
    resultat : str = ""

    phrase = normalizeTexte(phrase)

    cle = normalizeTexte(cle)

    longueurCLe = len(cle)
    
    for element in range(len(phrase)):
        if phrase[element] in alphabet:
            resultat += alphabet[(alphabet.index(phrase[element]) - alphabet.index(cle[element % longueurCLe])) % TAILLE_ALPHABET]
        else:
            resultat += phrase[element]
    return resultat


print("MENU :")
print("1. Chiffrer un message")
print("2. Déchiffrer un message")
print("3. Quitter")

choix = input()



if choix == "1":
    phrase = input("Entrez le message à chiffrer : ")
    cle = input("Entrez la clé de chiffrement : ")
    print("Votre message chiffré : " + chiffre_vigenere(phrase, cle))

elif choix == "2":
    phrase = input("Entrez le message à déchiffrer : ")
    cle = input("Entrez la clé de déchiffrement : ")
    print("Votre message déchiffré : " + dechiffre_vigenere(phrase, cle))

elif choix == "3":
    print("Au revoir !")