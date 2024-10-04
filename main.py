from ChiffrementVigenere import *

if __name__ == "__main__" :
    print("MENU :")
    print("1. Chiffrer un message")
    print("2. Déchiffrer un message")
    print("3. Trouver la taille d'une clé dans un fichier")
    print("4. Quitter")
    choix = input()
    if choix == "1":
        # Changer les input("") par un string pour les tests avec une clé et un texte précis
        texte = input("Entrez le message à chiffrer : ")
        cle = input("Entrez la clé de chiffrement : ")
        print("Votre message chiffré : " + chiffreVigenere(texte, cle))

    elif choix == "2":
        # Changer les input("") par un string pour les tests avec une clé et un texte précis
        texte = input("Entrez le message à déchiffrer : ")
        cle = input("Entrez la clé de déchiffrement : ")
        print("Votre message déchiffré : " + dechiffreVigenere(texte, cle))

    elif choix == "3":
        chemin_fichier = input("Entrez le chemin du fichier à lire : \n")
        methodeKasiski(chemin_fichier)

    elif choix == "4":
        print("Au revoir !")

    else:
        print("Choix invalide")