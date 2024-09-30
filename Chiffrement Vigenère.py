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







