import doctest


def cifrarClave(frase, clave):
    """
        este metodo es capas de cifrar un texto pasado atraves
        del metodo de cesar 

        >>> cifrarClave ("Argentina Programa", 5)
        'FWLJSYNSF UWTLWFRF'

        >>> cifrarClave ("Campeon Mundial", 9)
        'LJVYNXW VDWMRJU'

        >>> cifrarClave ("Fernet con Coca", 7)
        'MLYULA JVU JVJH'

        >>> cifrarClave ("Cifrado Cesar", 4)
        'GMJVEHS GIWEV'

        >>> cifrarClave ("Folclore y mate", 11)
        'QZWNWZCP J XLEP'

        >>> cifrarClave ("GRACIAS MESSI!!", 15)
        'VGPRXPH BTHHX!!'

        >>> cifrarClave ("Domingo de asado y vino!", 8)
        'LWUQVOW LM IAILW G DQVW!'

        >>> cifrarClave ("Aprendimos algo de Python??", 1)
        'BQSFOEJNPT BMHP EF QZUIPO??'

        >>> cifrarClave("HOLA MUNDO", 5)
        'MTQF RZSIT'

        >>> cifrarClave("#programarQuemaCoco", 35)
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


doctest.testmod()
# frase a cifrar
frase = input("Ingrese una frase para cifrar -> ")  

# desplazamiento en el diccionario
clave = int(input("Ingresar la cantidad de desplazamiento ->"))

cifrarClave(frase, clave)
