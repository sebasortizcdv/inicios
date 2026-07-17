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

#27 TAREA

# lista = [1,3,4,5,6,7,9,1]
# resultado = 0
# for numero in lista:
#     resultado = resultado + numero

# print(resultado)

#28 TAREA

# resultado = 0 
# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] 
# for numero in lista:
#     if numero%2 == 0:
#          resultado = resultado + numero
#     else:
#         resultado = resultado - numero
# print(resultado)

#29 TAREA

# gatillo = ""
# while gatillo != "soltar":
#     gatillo = input("Por favor, escribe [fuego] para disparar y [soltar] para detener el arma: ").lower()

#     if gatillo == "fuego":
#         for rafaga in range(1,4):
#             print(F'RATATATA [Bala nro {rafaga}]')
#     elif gatillo == "soltar":
#         print("Hasta la proxima!")

#30 TAREA

# for soldado in range(1,4):
#     flexiones = 0
#     print(f'Soldado numero {soldado}')
#     while flexiones < 5:
#         repeticion = input("Por cada flexion que haga este soldado presiona [ENTER]: ")
#         flexiones += 1
#         print(flexiones)
#     print("Alto! soldado aprobado!")

#31 TAREA 
# for camion in range(1,3):
#     print(f'Camion numero {camion}')
#     peso_total = 0
    
#     while peso_total < 20:
#         caja = int(input("Por favor, ingresa el peso de la caja que cargaras: "))
#         if peso_total + caja > 20:
#             print("Acabas de exceder el peso maximo, por favor, nivela tu carga")
#         else:
#             peso_total = peso_total + caja
#             print(f'Genial! llevas {peso_total} toneladas')
#     print(f'Camion numero {camion} cargado, siguiente.')
# print("camiones cargados! puedes comenzar tu viaje")

#32 TAREA
# carrito = ["pan", "queso", "huevos"]
# for productos in carrito:
#     print(f'llevas {productos} en tu carrito sebastian')

#33 TAREA
# invitados = []
# while len(invitados) < 2:
#     nuevo_invitado = input("Por favor, ingrese los nombres de los invitados a tu fiesta: ")
#     invitados.append(nuevo_invitado)
# print("Genial, acabamos de completar el numero de los invitados")
# print(invitados)

#34 TAREA
# numeros_impares = []
# numeros_pares = []
# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# for numero in numeros:
#     if numero%2 == 0:
#         numeros_pares.append(numero)
#     else:
#         numeros_impares.append(numero)
# print(numeros_pares)
# print(numeros_impares)

# 35 TAREA

# invitados = []
# negra = ["gabriela", "valeria", "aniuska", "laura"]

# while len(invitados) < 3:
#     nombre = input("Sebastian, por favor ingrese solamente 3 que estan invitados a la fiesta: ").lower()
#     invitados.append(nombre) 

# for amigo in invitados:
#     if amigo in negra:
#         print("Mujer del diavlo, no puedes pasar")
#     else:
#         print("Felicidades primo hermano, puedes pasar a la despedida de soltero de sebastian")

# 36 TAREA

# nombres = []
# hombres = []
# mujeres = []

# for _ in range(5):
#     nombre = input("Por favor, ingrese los nombres que desea en la lista: ")
#     nombres.append(nombre)

# for nombre in nombres:
#     if nombre[-1] == "a":
#         mujeres.append(nombre)
#     else:
#         hombres.append(nombre)

# print(mujeres)
# print(hombres)

#37 TAREA

# numeros_ingresados = []
# grandes = []
# pequenos = []

# for _ in range(6):
#     numero = input("Por favor, ingrese 6 numeros aleatorios: ")
#     numeros_ingresados.append(numero)

# for numero in numeros_ingresados:
#     if int(numero) >= 100:
#         grandes.append(numero)
#     else:
#         pequenos.append(numero) 
# print(grandes)
# print(pequenos)   

# 38 TAREA

# palabra_completa = []
# empieza_vocal = []
# lista = []
# for _ in range(6):
#     nombre = input("Por favor, ingresa cualquier nombre o letra, lo que quieras : ").lower()
#     lista.append(nombre)

# for letra in lista:
#     if len(letra) > 0:
#         if letra[0] in "aeiou":
#             empieza_vocal.append(letra)
#         else:
#          palabra_completa.append(letra)

# print(palabra_completa)
# print(empieza_vocal)

# 39 TAREA
# El Cajero Selectivo (Listas y Filtros Numéricos)
# En este ejercicio, tú serás el que clasifica el dinero en un banco. Tu trabajo es separar las "transacciones grandes" de las "pequeñas".

# numeros_ingresados = []
# grandes = []
# pequenos = []

# for _ in range(6):
#     numero = int(input("Por favor, escriba el numero que quiere ingresar: "))
#     numeros_ingresados.append(numero)

# for numero in numeros_ingresados:
#     if numero >= 100: 
#         grandes.append(numero)
#     else:
#         pequenos.append(numero)
# print(grandes)
# print(pequenos)

#40 TAREA

# productos = ["fresa","cambur","melon","uva","coco"]
# for fruta in productos:
#     precio = 0
#     while precio <= 0:
#         precio = int(input(f'Ingrese el precio de {fruta}: '))
#     print("Precio registrado")

# print(productos)

#41 TAREA

# atletas = []

# for _ in range(1,4):
#     kilometros = 0
#     nombre = input("Por favor, ingrese el nombre de sus atletas: ")
#     atletas.append(nombre)

#     for _ in range(1,3):
#         sesiones = 0
#         distancia = int(input("Ingrese la distancia recorrida: "))
#         kilometros += distancia
        
#     print(f'La distancia recorrida de {nombre}, es: {kilometros}Km')

#42 TAREA 

# lista_lacteos = []
# lista_limpieza = []
# categorias = ["lacteos","limpieza"]
# for categoria in categorias:
#     proceso = input(f'iniciando carga de: {categoria} [oprima ENTER para continuar...]')

#     for _ in range(1,3):
#         producto = input("Por favor, ingrese el nombre del producto: ")
        
#         if categoria == "lacteos":
#             lista_lacteos.append(producto)
#         else:
#             lista_limpieza.append(producto)
# print(lista_lacteos)
# print(lista_limpieza)

#43 TAREA

# total_herramientas = []

# for caja in range(1,3):
#     print(f'Caja {caja}')

#     for _ in range(4):
#         herramienta = input("Por favor, ingrese las herramientas que guardara: ").lower()
#         if herramienta == "pesado":
#             break
#         total_herramientas.append(herramienta)
# print(total_herramientas)

# 44 TAREA

# usuarios = ["sebastian", "admin"]
# clave = 1234

# for usuario in usuarios:
#     print(usuario)
#     peticion = int(input("Por favor, ingrese su clave: "))

#     while peticion != clave:
#         print("Contrasena incorrecta")
#         peticion = int(input("Vuelva a ingresar su clave: "))
    
#     print(f'Clave correcta para {usuario}')

# 45 TAREA

# for usuario in range(1,3):
#     print(f'Usuario {usuario}')
#     saldo_disponible = 100
#     retiro = int(input("Por favor, seleccione la cantidad a retirar: "))
    
#     while retiro > 50:
#         retiro = int(input("Monto excedido, por favor ingrese un monto valido: "))

#     saldo_disponible -= retiro 
#     print(f'Acaba de retirar {retiro} de su cuenta')   
#     print(f'su saldo disponible es de: {saldo_disponible}')  

#46 TAREA 

# cajas_existentes = 20

# while cajas_existentes != 0:
#     solicitud = int(input("Por favor, ingrese la cantidad de cajas a retirar: "))

#     if solicitud <= cajas_existentes:
#         cajas_existentes -= solicitud
#         print(f'Quedan {cajas_existentes} cajas en el almacen.')

#     else:
#         print("Por favor, ingrese una cantidad valida")

# print("Bodega vacia.")

#47 TAREA

# cajas = 10

# while cajas >= 0:
#     solicitud = int(input("Por favor, ingrese el numero de cajas para sacar: "))

#     if solicitud == -1:
#         print("Solicitud cancelada por el usuario")
#         break
#     elif solicitud > cajas:
#         print("Sin existencia de cajas suficientes")
#     else:
#         cajas -= solicitud
#         print(f'Quedan {cajas} cajas disponibles')

# EJEMPLO

# lista_compras = [["hades", 25], ["silksong", 15], ["baldurs", 34]]
# catalogo_steam = dict(lista_compras)
# print(catalogo_steam["hades"])

# 48 TAREA 

# lista_inicial = ["salto de cuerda", "sentadilla", "flexiones"]

# ejercicio_extra = "burpees"
# eliminar = ""

# print(lista_inicial)

# ejercicio = input("Presiona [ENTER] para agregar (Burpees) a tu rutina: ")
# lista_inicial.append(ejercicio_extra)

# print(lista_inicial)

# while eliminar != "salto de cuerda" and eliminar != "sentadilla" and eliminar != "flexiones":
#     eliminar = input("deseas eliminar algun ejercicio de esta lista?: ").lower()  

#     if eliminar == "salto de cuerda":
#         lista_inicial.remove("salto de cuerda")
#     elif eliminar == "sentadilla":
#         lista_inicial.remove("sentadilla")
#     elif eliminar == "flexiones":
#         lista_inicial.remove("flexiones")
#     elif eliminar == "burpees":
#         lista_inicial.remove("burpees")

# print(lista_inicial)
# print("Comenzamos con la rutina!")

# 49 TAREA

# piernas = ["sentadilla", "estocada", "salto"]
# explosividad = ["pique", "salto", "burpees"]

# print(set(piernas + explosividad))

#50 TAREA

# limpios = []
# lista = ["  SENIAT", "seniat", "Alcaldía", "ALCALDÍA  ", "Corpoelec", "corpoelec"]

# for nombre in lista:   
#     limpios.append(nombre.strip().lower())
#     print(limpios)

# print(set(limpios))

# 51 TAREA LO HIZO GEMINI

# nombres = ["sebastian", "fabian", "carlos", "valeria", "jose", "luis"]
# nombre = ""

# while nombre not in nombres:
        
#     if nombre != "":
#         print("nombre no esta en la lista")
#     nombre = input("Ingrese su nombre: ").strip().lower()
    

# print("Identidad confirmada.")

#52 TAREA

# encontrado = False
# lista = [
# {"modelo": "skyline R34", "estado": "caja"}, {"modelo": "datsun 510", "estado": "caja"}, {"modelo": "silvia", "estado": "sin caja"}
# ]

# while encontrado != True:
#     deseado = input("Por favor ingrese el nombre del modelo deseado: ").strip().lower()
#     for carro in lista:
#         if carro["modelo"] == deseado:
#             encontrado = True
#             print(f'El carro {carro["modelo"]} esta {carro["estado"]}')
#             break

#53 TAREA

# capacidad = ""
# equipos = [{"nombre": "pc gamer", "watts": 400}, {"nombre": "mini pc", "watts": 65}, {"nombre": "monitor", "watts": 35}]


# while capacidad != "salir":
#     capacidad = input("Por favor, ingrese la capacidad total de WATTS que busca: ")
#     if capacidad == "salir":
#         break
#     for equipo in equipos:
#         if equipo["watts"] <= int(capacidad):
#             print(f'{equipo["nombre"]}')

# 54 TAREA

# sensores = [{"componentes":"cpu", "grados": 95}, {"componentes":"gpu", "grados": 97}, {"componentes":"ram", "grados": 76}]
# limite = ""

# while limite != "cerrar":
#     limite = input("Por favor, ingrese la termperatura limite: ")
#     if limite == "cerrar":
#         break

#     for sensor in sensores:
#         if sensor["grados"] > int(limite):
#             print(f'{sensor["componentes"]} esta caliente {sensor["grados"]}')
#         else:
#             print(f'{sensor["componentes"]} esta estable')

#55 TAREA
# Imagina que no solo quieres saber la temperatura, sino también qué marca es el componente, para saber a quién reclamar la garantía si se quema.

# Tu Misión:

# Tus datos: Crea una lista llamada pc_setup con 3 diccionarios. Cada uno debe tener tres llaves: {"parte": "...", "marca": "...", "temp": ...} (ej: "cpu", "amd", 95).

# El Objetivo: El usuario ingresa un límite de temperatura.

# La Lógica:

# El while se repite hasta escribir "off".

# El for debe buscar los componentes que superen ese límite.

# Si lo supera, debe imprimir un mensaje más completo: "Alerta: El [parte] marca [marca] llegó a [temp]°C".

# Si está bien, simplemente imprime: "[parte] funcionando correctamente".
        
# pc_setup = [{"parte": "cpu", "marca": "amd", "temp": 96}, {"parte": "gpu", "marca": "nvidia", "temp": 99}, {"parte": "ram", "marca": "samsung", "temp": 70}]
# limite = ""

# while limite != "off":
#     limite = input("Por favor, ingrese la temperatura limite buscada: ")
#     if limite == "off":
#         break

#     for componente in pc_setup:
#         if componente["temp"] > int(limite):
#             print(f'[ALERTA]: EL componente: {componente["parte"]}, marca: {componente["marca"]} llego a: {componente["temp"]}')
#         else:
#             print(f'{componente["parte"]} funcionando correctamente')

# 14 * 4

# age = 14 * 4
# print(age)

# def promedio(num_1, num_2, num_3):
#     return int((num_1 + num_2 + num_3)/3)
# resultado = promedio(5, 9, 3)
# print(resultado)

# def sum_numeros(numeros):
#     total = 0
#     for numero in numeros:
#         total += numero
#     resultado = total
#     return total

# resultado = sum_numeros([1, 2, 3])
# print(resultado)


# def suma(*numeros):
#     resultado = sum(numeros)
#     print(resultado)

# suma(1,2,3,4,5,6)

# # Example of using .items()
# my_dict = {"name": "Alice", "age": 25}

# for key, value in my_dict.items():
#     print(f"{key}: {value}")














   
        





    
    








        
    




    
    

















        







    
       


    

    
            

    

    




  


    


            

        
        










    
  
   

