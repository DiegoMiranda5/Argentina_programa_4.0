import doctest


def cifrado_cesar(frase, clave):
    """
        este metodo es capas de cifrar un texto pasado atraves
        del metodo de cesar 

        >>> cifrado_cesar ("Argentina Programa", 5)
        'FWLJSYNSF UWTLWFRF'

        >>> cifrado_cesar ("Campeon Mundial", 9)
        'LJVYNXW VDWMRJU'

        >>> cifrado_cesar ("Fernet con Coca", 7)
        'MLYULA JVU JVJH'

        >>> cifrado_cesar ("Cifrado Cesar", 4)
        'GMJVEHS GIWEV'

        >>> cifrado_cesar ("Folclore y mate", 11)
        'QZWNWZCP J XLEP'

        >>> cifrado_cesar ("GRACIAS MESSI!!", 15)
        'VGPRXPH BTHHX!!'

        >>> cifrado_cesar ("Domingo de asado y vino!", 8)
        'LWUQVOW LM IAILW G DQVW!'

        >>> cifrado_cesar ("Aprendimos algo de Python??", 1)
        'BQSFOEJNPT BMHP EF QZUIPO??'

        >>> cifrado_cesar("HOLA MUNDO", 5)
        'MTQF RZSIT'

        >>> cifrado_cesar("#programarQuemaCoco", 35)
        '#YAXPAJVJAZDNVJLXLX'

    """

    fraseM = frase.upper()
    fraseCifrada = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #recorre el string 
    for caracterCifrar in fraseM:
        #comprueba que el caracter del string se encuentre dentro de nuesto abecedario
        if caracterCifrar in abc:
            fraseCifrada += abc[(abc.index(caracterCifrar)+clave) % len(abc)]
        else:
            fraseCifrada += caracterCifrar

    return fraseCifrada

def decifrado_Cesar(frase, clave):
    fraseM = frase.upper()
    fraseCifrada = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #recorre el string
    for caracterCifrar in fraseM:
        #comprueba que el caracter del string se encuentre dentro de nuesto abecedario
        if caracterCifrar in abc:
            fraseCifrada += abc[(abc.index(caracterCifrar)-clave) % len(abc)]
        else:
            fraseCifrada += caracterCifrar

    return fraseCifrada


doctest.testmod()
