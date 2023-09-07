import doctest

def cifrado_atbash(frase):
    
    """
        este metodo es capas de cifrar un texto pasado atraves
        del metodo de cesar 

        >>> cifrado_atbash ("Argentina Programa")
        'ZITVMGRMZ KILTIZNZ'

        >>> cifrado_atbash ("Campeon Mundial")
        'XZNKVLM NFMWRZO'

        >>> cifrado_atbash ("Fernet con Coca")
        'UVIMVG XLM XLXZ'

        >>> cifrado_atbash ("Cifrado Cesar")
        'XRUIZWL XVHZI'

        >>> cifrado_atbash ("Folclore y mate")
        'ULOXOLIV B NZGV'

        >>> cifrado_atbash ("GRACIAS MESSI!!")
        'TIZXRZH NVHHR!!'

        >>> cifrado_atbash ("Domingo de asado y vino!")
        'WLNRMTL WV ZHZWL B ERML!'

        >>> cifrado_atbash ("Aprendimos algo de Python??")
        'ZKIVMWRNLH ZOTL WV KBGSLM??'

        >>> cifrado_atbash("HOLA MUNDO")
        'SLOZ NFMWL'

        >>> cifrado_atbash("#programarQuemaCoco")
        '#KILTIZNZIJFVNZXLXL'
        
        >>> cifrado_atbash("el ñandu del año")
        'VO MZNWF WVO ZML'
    """
    
    fraseM = frase.upper()
    
    fraseCifrada = ""
    
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abc_Invertido = abc[::-1]
    
    for caracter in fraseM:
        if caracter in abc:
            fraseCifrada += abc_Invertido[abc.index(caracter)]
        else:
            fraseCifrada += caracter
            
    return fraseCifrada
            
doctest.testmod()
frase = input("Ingre una frase a cifrar -> ")

print(cifrado_atbash(frase))