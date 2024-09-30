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


