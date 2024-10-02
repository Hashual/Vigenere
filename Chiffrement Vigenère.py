import unicodedata
import string

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