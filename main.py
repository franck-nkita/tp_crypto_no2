from algo import *

while 1:
    print(" \n \n \nBonjour, faite votre choix.")

    print("\n1. teste rapide"
          "\n 2. entre votre message a crypter"
          "\n 3. sortir")
    
    choix = input("\n\n entre votre choix : ")

    if choix == "1":
        print("\n le message d'exemple est : Bonjour mon frere.")
        exemple = exem("\n Bonjour mon frere")
        print(f"\n voici le resultat : {exemple}")

    elif choix == "2":
        mm = input(" \nentrez votre texte : ")
        message = crypt_nkita(mm)
        print(f" \nvoici le message crypter{message}")

    else:
        break
