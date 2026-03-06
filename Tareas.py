# #1 TAREA
# nombre = input("Un gusto saludarte, por favor inserte su nombre:")
# edad = int(input("Por favor, ahora coloque su edad: "))
# if edad >= 18:
#     print(f'Genial, {nombre}, eres mayor de edad, puedes pasar')
# else:
#     print(f'Lo sentimos mucho, {nombre}, no tienes permitido pasar')

# #2 TAREA

# r1="si"
# r2="no"

# nombre = input("Bienvenido, inserte su nombre: ")      
# invitacion = input("Tiene invitacion?: ").lower()
# edad = int(input("Por favor, inserte su edad:" ))
# entrada = int(input("ingrese el valor de dinero que lleva con usted: "))
# if invitacion == r1 or edad >= 18 and entrada >= 100:
#     print(f'Un placer, {nombre}, puede pasar a la fiesta')
# else:
#     print(f'Lo sentimos mucho, {nombre}, no podemos permitirle el paso')

# #3 TAREA

# nombre = input("Igresar nombre: ")
# nota = int(input("Por favor, ingresar la nota de su examen: "))
# if nota > 100: 
#     print("por favor, ingresar una nota valida")
# else:

#     if nota >= 90:
#         print(f'Felicidades, {nombre}, gran trabajo')
#     elif nota >= 70:
#         print(f'Muy bien, {nombre}, aprobaste')
#     elif nota >= 50:
#         print(f'Pasaste rapando, te salvaste')
#     else:
#         print(f'{nombre}, mas bruto y eres chavista, anda a estudiar')   

# #4 TAREA

# name = input("por favor, ingrese su nombre: ")
# price = float(input("ingrese el valor total de su compra: "))
# tag = input("Ingrese el color de su etiqueta: ").lower()
# total_price_1 = (price*0.80)
# total_price_2 = (price*0.90)

# while tag != 'rojo' and tag != 'verde':
#     tag = input("Por favor ingrese un color valido entre (rojo/verde): ").lower()


# if tag == 'rojo' and price >= 500:
#     print(f'estimado {name}, usted cuenta con un descuento del 20%')
#     print(f'{name}, a continuacion adjuntamos su recibo de pago: ')
#     print(f'[cliente: {name}] [Precio original: {price}] [Descuento del: 20%] [PRECIO TOTAL: {total_price_1}]')

# elif tag == 'verde' or price > 800:
#     print(f'Estimado {name}, usted cuenta con un descuento del 10%')
#     print(f'{name}, a continuacion adjuntamos su recibo de pago: ')
#     print(f'[cliente: {name}] [Precio original: {price}] [Descuento del: 10%] [PRECIO TOTAL: {total_price_2}]')

# else:
#     print(f'El precio total de su compra es: {price}')

# #5 TAREA

# tasa = float(input("Por favor, ingrese tasa BCV del dia de hoy: "))

# while tasa <= 0:
#     tasa = float(input("Por favor ingrese un valor mayor a 0: "))

# bolivares = float((input("Porfavor ingrese la cantidad de bolivares que desea cambiar: ")))

# dolares = (bolivares/tasa)
# if dolares >= 1000:
#     print(f'Recibo VIP: {dolares: .2f} USD. [TASA APLICADA: {tasa}]')
# else:
#     print(f'Recibo estandar: {dolares: .2f} USD [TASA APLICADA: {tasa}]')

# #6 TAREA
# opcion = input("por favor, seleccione una opcion:\n1. Suma\n2. Resta\n0. Salir\n").lower()

# while opcion != "0" and opcion != "salir":
#     if opcion == "1" or opcion == "suma":
#         num_1 = float(input("Por favor ingresa tu primer digito: "))
#         num_2 = float(input("Por favor ingresa tu segundo digito: "))
#         print(f'El resultado es {num_1+num_2}')
#         opcion = input("por favor, seleccione una opcion:\n1. Suma\n2. Resta\n0. Salir\n").lower()


#     elif opcion == "2" or opcion == "resta":
#         num_1 = float(input("Por favor ingresa tu primer digito: "))
#         num_2 = float(input("Por favor ingresa tu segundo digito: "))
#         print(f'El resultado es {num_1-num_2}')
#         opcion = input("por favor, seleccione una opcion:\n1. Suma\n2. Resta\n0. Salir\n").lower()

#     else:
#         opcion = input("por favor, seleccione una opcion:\n1. Suma\n2. Resta\n0. Salir\n").lower()

# # #7 TAREA

# # order = input("Por favor escribe una orden:")
# # for number in range(1,4):
# #     print(f'{number} {order.upper()}')
# # print("todos a sus puestos!")

# #8 TAREA
# # for invitado in range(1,6):
# #     if invitado == 3:
# #         print(f'Invitado {invitado}, espera! necesito ver tu entrada')
# #     else:
# #         print(f'Invitado {invitado}: bienvenido a la fiesta :D')

# #9 TAREA
# # for luz in range(1,7):
# #     if luz == 1 or luz == 2:
# #         print(f'luz {luz}, ROJO - Detenerse')
# #     elif luz == 3 or luz == 4:
# #         print(f'luz {luz}, AMARILLO - Ojo pelao')
# #     else:
# #         print(f'Luz {luz}, VERDE - Puede avanzar')
    

# #10 TAREA
# # for sec in range(5,0,-1):
# #     print(f'[T-mins] {sec}...')
# #     if sec == 3:
# #         print("Chequeo de motores")
# # print("ingnición") 

# #11 TAREA
# saldo = 100
# pin_correcto = 2312

# pin = int(input("Por favor, ingrese PIN de seguridad: "))
# while pin != pin_correcto:
#     pin = int(input('PIN incorrecto, por favor vuelva a intentarlo: '))


# retiro = float((input("por favor ingrese cantidad a retirar: "))) 
# while retiro <= 0 or retiro > saldo:

#     if retiro > saldo:
#         retiro = float(input("Por favor, ingrese un valor menor al que tiene "))
#     else:
#         retiro = float(input("Por favor, ingrese un valor mayor a 0"))

# for _ in range(3):
#     print("Contando dinero...")
# if retiro == 100:
#     print(f'Atencion, su cuenta quedara sin dinero. Realizando operacion: {(saldo - retiro): .2f}')
# else:
#     print(f'Realizando retiro: {(saldo - retiro): .2f}')

# #12 TAREA
# secret_num = 10
# name = input("Por favor, ingrese su nombre: ")
# numero = int(input("por favor, intente adivinar el numero secreto: "))
# while numero != 10:
#     if numero > 10:
#         print("Incorrecto, una pista, el numero que buscas es menor al tuyo")
#     else:
#         print("Incorrecto, una pista, el numero es mayor al que buscas")
#     numero = int(input("Por favor ingrese un nuevo digito: "))
# print(f'Felicidades {name}, numero correcto!!')
    
# #
# vocales = ["a","e","i","o","u"]
# palabra = input("Por favor, ingresa una palabra o frase corta: ").lower()
# for letra in palabra:
#     if letra in vocales:
#         print(f'La {letra} es una vocal')
#     else:
#         print(f'{letra} No es una vocal')

# # 14 TAREA
# numero_secreto = 69
# intentos = 1
# numero = int(input("Por favor, intente adivinar el numero secreto: "))
# while numero != numero_secreto and intentos < 3:
#     if numero > 69:
#         print("El numero que buscas es menor")
#     else:
#         print("el numero que buscas es mayor ")
#     numero = int(input("Incorrecto, por favor intente con otro digito: "))
#     intentos = intentos + 1
# if intentos == 3 and numero_secreto != numero:
#     print("Lo sentimos, no tienes mas intentos")
# else:    
#     print(f'Felicidades! has dado con el numero, tu numero de intentos es: {intentos}')

# 15 TAREA
# for caja in range (1,4):
#     print(f'Iniciando caja numero {caja}')
#     productos_validos = 0

#     while productos_validos < 4:
#         estado = input("Por favor, ingrese un estado valido entre bien/mal: ").lower()
#         if estado == "bien":
#             productos_validos = productos_validos + 1
#             print(f'Genial, llevas {productos_validos} productos validos')
#         else:
#             print("producto descartado, por favor, intente con otro")
# print("Porduccion completa, Sebastian")

#16 TAREA
# cajas = int(input("Por favor, ingrese el total de cajas a procesar: ")) 

# for caja in range(1,cajas+1):
#     print(f'Caja nro: {caja}') 
#     productos = int(input("Cuantos productos necesita esta caja?: "))

#     conteo = 0

#     while conteo < productos:
#         estado = input("Por favor, ingrese en estado valido entre [bien/mal]: ").lower()
#         if estado == "bien":
#             conteo = conteo + 1
#             print(f'Genial, llevas {conteo}, productos validos')
#         else:
#             print("Producto descartado, por favor, ingrese nuevamente otro: ")
#     print(f'Genial, aun quedan por validar {cajas - caja}')

#17 TAREA

# for serie in range(1,4):
#     print(f'Serie Nro: {serie}') 
#     flexiones = int(input("Cuantas flexiones haremos en esta serie?: ")) 

#     conteo_correcto = 0

#     while conteo_correcto < flexiones:
#         estado = input("Por favor ingrese si su flexion fue [bien/mal]: ")
#         if estado == "bien":
#             conteo_correcto = conteo_correcto + 1
#             print(f'Genial! llevas {conteo_correcto} flexiones')
#         else:
#             print("Rep invalida, sigue intentandolo")
#     print("Serie terminada, descansa un minuto.")

#18 TAREA 

# pin_seguridad = "1234"
# verif = input("Por favor, ingresa el pin de seguridad: ")

# while verif != pin_seguridad:
#     print("PIN incorrecto, por favor vuelva a intentarlo: ")
#     verif = input("Por favor, ingresa el PIN de seguridad nuevamente: ")

# print("Bienvenido, Sebastian.")

#19 TAREA

# intentos = 0
# for ronda in range(1,4):
#     print(f'Ronda {ronda}')
#     meta = 2
#     aciertos = 0

#     while aciertos < meta:
#         flechazos = input("Dio en el blanco? [si/no]: ").lower()
#         if flechazos == "si":
#             aciertos = aciertos + 1
#             print(f'Genial, llevas {aciertos} aciertos')
#         else:
#             print("Buen intento, sigue intentandolo!")
#         intentos = intentos + 1
# print(f'Fina! la cantidad total de intentos fue: {intentos}')

# 20 TAREA

# decision = ""

# for producto in range(1,4):
#     print(f'producto Nro {producto}')
#     while decision != "aprobado" and decision != "rechazado":
#         decision = input("Por favor, ingrese el estado del producto [aprobado/rechazado]: ")
        
#     print(f'confirmado, el producto ha sido {decision}')
#     decision = ""

#21 TAREA

# stock_etiquetas = 10
# cajas = int(input("Por favor, indique cuantas cajas seran procesadas: "))

# for caja in range(1,cajas+1):
#     productos_totales = int(input("Por favor, indique cuantos productos buenos debe tener cada caja: "))
#     productos_revisados = 0

#     while productos_revisados < productos_totales and stock_etiquetas > 0:
#         estado = input("Por favor indique el estado del producto [bien/mal]: ")
#         if estado == "bien":
#             productos_revisados += 1
#             stock_etiquetas -= 1

#     if stock_etiquetas == 0:
#         print("Atencion, se agotaron las etiquetas D:")
#         break
#     else:
#         print(f'Quedan el almacen {stock_etiquetas}')

#22 TAREA
# for piso in range(1, 4):
#     print(f"--- Llegando al Piso {piso} ---")
#     puerta = "abierta" 
    
#     while puerta != "si":
#         puerta = input("¿Puerta cerrada para poder arrancar? [si/no]: ").lower()
        
#         if puerta == "si":
#             print("Puerta asegurada. ¡Subiendo!")
#         else:
#             print("ERROR: El ascensor no se mueve con la puerta abierta.")

# print("¡Sebastián, has llegado al último piso con éxito!")

# #23 TAREA

# for cuadro in range(1,4):
#     print(f'Cuadro nro {cuadro}')
#     golpes = 0

#     while golpes < 3:
#         input("Por favor, presiona [ENTER] para martillar: ")
#         golpes += 1
#         print(f'Genial, llevas {golpes} martillazos')
#     print("Cuadro colgado")

#24 TAREA

# for torta in range(1,3):
#     print(f'Torta {torta}')
#     estado = ""

#     while estado != "listo":
#         estado = input("Por favor, ingrese el estado de su torta [listo]: ").lower()
#         if estado == "listo":
#             print("Genial, torta finalizada!")
# print("Ya terminamos las tortas que necesitabas!")

#25 TAREA

# verif = "1234"
# for caja_fuerte in range(1,3):
#     print(f'Caja nro {caja_fuerte}')
#     intentos = 0
#     clave = ""

#     while clave != verif and intentos < 3:
#         clave = input("por favor, ingrese la clave de seguridad: ")
#         intentos += 1
#         print("Acceso denegado")
    
#     if clave == verif:
#         print("Acceso concedido con exito")
#     elif intentos == 3:
#         print ("El acceso fue bloqueado por cantidad de intentos")
        
#26 TAREA

# total_general = 0
# for estante in range(1,3):
#     sanos = 0
#     total_revisados = 0
#     print(f'Estante nro {estante}')

#     while sanos < 3:
#         estado = input("Por favor, ingrese el estado del producto [sano/malo]: ").lower()
#         total_general += 1
#         total_revisados += 1
#         if estado == "sano":
#             sanos += 1
#     print(f'Proceso finalizado revisaste {total_revisados} productos')

# print(f'Total de productos revisados {total_general}')

    

    
            

    

    




  


    


            

        
        










    
  
   

