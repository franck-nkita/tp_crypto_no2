def crypt_nkita(texte):
    crypt_value = 0
    cle = "NKITA"

    for i, char in enumerate(texte):
        crypt_value += ord(char)
        crypt_value += ord(cle[i % len(cle)])
        crypt_value = (crypt_value * 31) % 1000000

    return crypt_value



def exem(mss: str):
    mss
    resultat = crypt_nkita(mss)
    return resultat
