import unicodedata
import string

alphabet = string.ascii_uppercase
TAILLE_ALPHABET = 26

def normaliseTexte(texte: str) -> str:

    texte = unicodedata.normalize('NFD', texte)
    for letter in texte:
        if not letter.isalpha():
            texte = texte.replace(letter, '')

    texte = texte.upper()

    return texte

def chiffre_vigenere( phrase :str , cle : str) -> str:
    resultat : str = ""

    phrase = normaliseTexte(phrase)

    cle = normaliseTexte(cle)

    longueurCLe = len(cle)
    
    for element in range(len(phrase)):
        if phrase[element] in alphabet:
            resultat += alphabet[(alphabet.index(phrase[element]) + alphabet.index(cle[element % longueurCLe])) % TAILLE_ALPHABET]
        else:
            resultat += phrase[element]
    return resultat

def dechiffre_vigenere( phrase :str, cle : str) -> str :
    resultat : str = ""

    phrase = normaliseTexte(phrase)

    cle = normaliseTexte(cle)

    longueurCLe = len(cle)
    
    for element in range(len(phrase)):
        if phrase[element] in alphabet:
            resultat += alphabet[(alphabet.index(phrase[element]) - alphabet.index(cle[element % longueurCLe])) % TAILLE_ALPHABET]
        else:
            resultat += phrase[element]
    return resultat


def kasiskiMethod(chemin_fichier : str) -> None:
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            fichier.close()
            contenu = normaliseTexte(contenu)

            repetitions = trouver_repetitions(contenu)
            if repetitions == {}:
                print("???")
            else:
                print("Répétitions trouvées : ", repetitions)

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def trouver_repetitions(texte, longueur_min=3) -> dict:
    repet : dict = {}
    
    for longueur in range(longueur_min, len(texte) // 2):
        for i in range(len(texte) - longueur):
            sous_chaine = texte[i:i+longueur]
            positions = []
            
            for j in range(i + longueur, len(texte) - longueur + 1):
                if texte[j:j+longueur] == sous_chaine:
                    positions.append(j)
            
            if positions:
                if sous_chaine in repet:
                    repet[sous_chaine].append(i)
                    repet[sous_chaine].extend(positions)
                else:
                    repet[sous_chaine] = [i] + positions
    return repet

    


print("MENU :")
print("1. Chiffrer un message")
print("2. Déchiffrer un message")
print("3. Déchiffrer un fichier")
print("4. Quitter")
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
    chemin_fichier = input("Entrez le chemin du fichier à lire : \n")
    kasiskiMethod(chemin_fichier)

elif choix == "4":
    print("Au revoir !")

else:
    print("Choix invalide")