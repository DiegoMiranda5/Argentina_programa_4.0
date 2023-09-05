import doctest

def equivalente_dhms(segundos):
    """
    La funcion equivalente_dhms realiza la equivalacion de segundos 
    a dias, horas, minutos y segundo
    >>> equivalente_dhms(3600)
    (0, 1, 0, 0)
    >>> equivalente_dhms(3666)
    (0, 1, 1, 6)
    """
    
    dias = segundos // 86400
    segundos %= 86400
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    
    return dias, horas, minutos, segundos

doctest.testmod()
segundos = int(input("Ingrese la cantidad de segundos -> "))
dias, horas, minutos, segundos = equivalente_dhms(segundos)
print(f"{dias}:{horas}:{minutos}:{segundos}")