nota = 1
cantNotas = 0
cantNotasAplazadas = 0
cantNotasAprobadas = 0
cantNotasPromocionados = 0

while nota != 0:
    nota = int(input("Ingrese una nota"))
    cantNotas += 1
    if nota < 4:
        cantNotasAplazadas += 1
    elif nota > 7:
        cantNotasPromocionados += 1
    else:
        cantNotasAprobadas += 1 
    
