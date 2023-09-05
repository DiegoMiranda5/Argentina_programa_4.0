nota = 1
cantNotas = 0
cantNotasAplazadas = 0
cantNotasAprobadas = 0
cantNotasPromocionados = 0

while nota != 0:
    nota = int(input("Ingrese una nota -> "))
    
    if nota == 0:
        print("Finalizando")
    elif nota < 4:
        cantNotasAplazadas += 1
        cantNotas += 1
    elif nota >= 4 and nota <= 7:
        cantNotasAprobadas += 1
        cantNotas += 1
    elif nota > 7:
        cantNotasPromocionados += 1
        cantNotas += 1
    elif nota < 1 or nota > 10:
        print("la nota ingresada es invalida")
    
if cantNotas > 0:
    print(f'Cantidad de aplazos:  {cantNotasAplazadas} ({round((cantNotasAplazadas*100)/cantNotas)}%)')
    print(f'Cantidad de aprobados:  {cantNotasAprobadas} ({round((cantNotasAprobadas*100)/cantNotas)}%)')
    print(f'Cantidad de promocionados:  {cantNotasPromocionados} ({round((cantNotasPromocionados*100)/cantNotas)}%)')