import cifrado_cesar
import cifrado_atbash
import archivo

def menu():
    print("---------------[Menu]--------------\n" +
          "|  1. Cifrar mensaje              |\n" +
          "|  2. Decifrar mensaje            |\n"+
          "|  3. Enviar mensaje cifrado      |\n"+
          "|  4. Consultar mensajes cifrados |\n"+
          "|  0. Salir                       |\n"+
          "-----------------------------------")

def validar_destinatario(destinatario=""):

    """
        Nos permite validar que el usuario de un espia sea valido
    """
    
    if len(destinatario) < 5 and len(destinatario) > 15:
        return False

    for caracter in destinatario:
        if not (caracter.isalnum() or caracter in ['-','.','_']):
            return False
        
    return True

def cifrar_mensaje():

    """
        Cifra un mensaje dejando al usuario elegir el modo de cifrado del mensaje
        esta funcion retorna una lista adonde el primer elemento es el tipo de cifrado
        y el segundo es el mensaje cifrado, en caso que el usuario eliga el cifrado cesar
        tambien nos guarada con el tipo de cifrado la cantidad de desplazamiento

            retornos dependiendo del cifrado elegido:
            
            cifrado cesar:
                return ['c' + clave de desplazamiento, mensaje cifrado]

            cifrado cesar:
                return ['a', mensaje cifrado]
    """

    mensaje = input("Ingrese el mensaje que desea cifrar -> ") #Se ingresa el mensaje a cifrar

    print("---------[Cifrada]-------\n" +
          "|  1. Cifrado Cesar     |\n" +
          "|  2. Cifrado Atbash    |\n"+
          "-------------------------")

    op = int(input("Ingrese el tipo de cifrado que se utilizara -> ")) #se ingresa el tipo de cifrado

    if op == 1: #se realiza el cifrado cesar

        clave = int(input("Ingrese el desplazamiento -> "))
        return [f"C{clave}", cifrado_cesar.cifrado_cesar(mensaje, clave)] 

    elif op == 2: #se realiza el cifrado atbash

        return ['A', cifrado_atbash.cifrado_atbash(mensaje)]

def decifrar_mensaje():

    """
        Nos permite decifrar un mensaje que haya sido cifrado con el cifrado cesar o atbash
        el usuario para poder decifrar el mensaje tiene que saber de antemano el tipo de cifrado
        utilizado, en caso de elegir el decifrado cesar aparte de mandar el mensaje tambien tiene
        que mandar la clave de desplazamiento utilizado
    """

    mensaje = input("Ingrese el mensaje que desea decifrar -> ")

    print("-------[Decifrada]-------\n" +
          "|  1. Decifrado Cesar   |\n" +
          "|  2. Decifrado Atbash  |\n" +
          "-------------------------")

    op = int(input("Ingrese el tipo de cifrado que se utilizara -> "))

    if op == 1:

        clave = int(input("Ingrese el desplazamiento -> "))
        return cifrado_cesar.decifrado_Cesar(mensaje, clave)

    elif op == 2:

        return cifrado_atbash.cifrado_atbash(mensaje)

def enviar_mensaje():

    """
        Nos permite ingresar un destinatario para mandar un mensaje cifrado y guardar en un archivo csv
        el nombre del espia, el tipo de cifrado utilizado y el mensaje cifrado
    """

    destinatario = input("Ingrese el espia destinatario del mensaje -> ") #ingreso para el espia destinatario
    try:
        if destinatario != '*':
            if validar_destinatario(destinatario):
                #genera un mensaje para un espia en especifico
                mensaje_cifrado = cifrar_mensaje()
                registro = [[destinatario] + mensaje_cifrado] #crea el registro a guardar
                print(registro)
                archivo.escribrir_en_archivo(registro) #se manda el registro creado para guardar
            else:
                print('Espia inexistente')
        else:
            #genera un mensaje para todos todos los espias
            mensaje_cifrado = cifrar_mensaje()
            registro = [["TODOS"] + mensaje_cifrado]
            archivo.escribrir_en_archivo(registro)
    except Exception:
        print("Ocurrio un ERROR en el envio del mensaje")

def mostrar_mensajes():

    """
        Muestra los mensaje guardados para un espia en especifico en el archivo con un formato de:
        
        listado de mensaje:
        ---------------------
        Todos: mensaje1
        ---------------------
        Todos: mensaje2
        ---------------------
        espia: mensaje3
        ---------------------
        espia: mensaje5
    """

    destinatario = input("Ingrese el espia destinatario del mensaje -> ")

    if validar_destinatario(destinatario):

        mensajes = archivo.leer_en_archivo()

        mensaje_para_todos = [] #Guarda los mensaje destinados para todos los espias
        mensaje_para_espia = [] #Guarda los mensaje destinados para un espia en especificos


        #Clasifica los mensajes guardados en el archivo
        for mensaje in mensajes:
            if mensaje[0] == "TODOS":
                mensaje_para_todos.append(f"{mensaje[0]}: {cifrado_atbash.cifrado_atbash(mensaje[2]) if mensaje[1] == 'A' else cifrado_cesar.decifrado_Cesar(mensaje[2], int(mensaje[1][1::]))}")
            elif mensaje[0] == destinatario:
                mensaje_para_espia.append(f"{mensaje[0]}: {cifrado_atbash.cifrado_atbash(mensaje[2]) if mensaje[1] == 'A' else cifrado_cesar.decifrado_Cesar(mensaje[2], int(mensaje[1][1::]))}")
        
        #Muestra los mensajes con un formato en especifico mostrado en el comentario general
        print("\nListado de Mensajes: ")
        print(f'{"-" * 90}')

        #Muestra los mensaje destinados para todos los espias
        for i in mensaje_para_todos:
            print(i)
            print(f'{"-" * 90}')

        #Muestra los mensaje destinados para el espia ingresado
        for i in mensaje_para_espia:
            print(i)
            print(f'{"-" * 90}')

    else:
        print("ALERTA: Usted es un intruso")

    archivo.cerrar_archivo()

opcion = 1
while opcion != 0:
    
    menu()
    opcion = int(input("Ingrese una opcion -> "))
    if opcion == 1:
        print(cifrar_mensaje()[1])
    elif opcion == 2:
        print(decifrar_mensaje())
    elif opcion == 3:
        enviar_mensaje()
    elif opcion == 4:
        mostrar_mensajes()
    elif opcion == 0:
        print("Finalizando ejecucion")
    else:
        print("Opcion invalida")