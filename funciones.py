# Crea una función llamada contar_caros(precios). La función debe recibir una lista de números (precios) y devolver cuántos de esos precios son mayores a 50.

# Entrada de ejemplo: [10, 55, 20, 100, 45]

# Resultado esperado: 2

# Tip: Vas a necesitar un acumulador (como el total = 0 de antes), pero en lugar de sumar el valor del número, debes sumarle 1 solo cuando se cumpla una condición (if).

# numero = 1

# def contar_caros(precios):
#     contador = 0
#     for precio in precios:
#         if precio >= 50:
#             contador += 1
#     print(contador)

# contar_caros([40, 50, 70,20])
# ----------------------------------------------------------------
# Tu próximo reto: "El Grito del Usuario" (Sin ayuda externa)
# Para este, intenta hacerlo tú solo. Si te trabas, dime exactamente en qué parte (ej: "no sé cómo crear una lista vacía" o "no sé cómo unir el signo de exclamación").

# Recordatorio de la tarea:
# Crea convertir_a_gritos(palabras). Recibe ["hola", "python"] y debe devolver ["HOLA!", "PYTHON!"].

# Pistas técnicas para ti:

# Mayúsculas: Si tienes una variable texto = "hola", puedes hacerla mayúscula usando texto.upper().

# Unir textos: Para pegar el "!", puedes usar el signo más: texto_en_mayusculas + "!".

# Guardar en lista: Para meter algo nuevo en una lista llamada bolso, usas bolso.append(lo_nuevo).

# def convertir_gritos(palabras):
#     mayusculas = []
#     for p in palabras:
#         grito = f'{p.upper()}!'
#         mayusculas.append(grito)
#     return(mayusculas)
# resultado = convertir_gritos(["Hola", "negro"])
# print(resultado)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Crea la función solo_pares(lista_numeros). Debe recibir una lista de números y devolver una nueva lista que contenga solo los que son pares.

# Pistas para que lo hagas solo:

# El "Bolso": Crea una lista vacía al principio (ej. pares = []).

# El Bucle: Recorre lista_numeros.

# La Condición: Usa el operador %. Si el resto de dividir entre 2 es cero (numero % 2 == 0), el número es par.

# El Guardado: Si se cumple la condición, usa .append().

# El Cierre: Devuelve la lista de pares al final.
    
# def solo_pares(lista_numeros):
#     pares = []
#     for numero in lista_numeros:
#         operacion = numero % 2
#         if operacion == 0:
#             pares.append(numero)
#     return(pares)
# resultado = solo_pares([2,3,5,7,10])
# print(resultado)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Crea una función llamada nombres_largos(lista_nombres). Debe recibir una lista de strings y devolver una nueva lista que contenga solo los nombres que tengan más de 5 letras.

# Tu "Caja de Herramientas" para este reto:

# Contar letras: En Python, para saber cuántas letras tiene un string, usas la función len(). Ejemplo: len("Sebastian") te devolvería 9.

# La Condición: Tu if ahora debe comparar si ese tamaño es mayor a 5.

# Entrada para probar: ["Ana", "Sebastian", "Ian", "Valeria", "Python"]
# Resultado esperado: ["Sebastian", "Valeria", "Python"]

# Tip de estudiante: No te olvides de la estructura que ya dominas:

# Crear la lista vacía.

# El bucle for.

# El if (esta vez usando len()).

# El .append() y el return.

# def nombres_largos(lista_nombres):
#     nombres = []
#     for nombre in lista_nombres:
#         if len(nombre) >= 5:
#             nombres.append(nombre)
#     return(nombres)
# resultado = nombres_largos(["Ana", "Sebastian", "Ian", "Valeria", "Python"])
# print(resultado)
# ---------------------------------------------------------------------------------------------------------------------------------------
# def sumar_positivos(numeros):
#     total = 0
#     for numero in numeros:
#         if numero > 0:
#             total += numero
#     return total
# resultado = sumar_positivos([2, -1, 4, 6, -35])
# print(resultado)
# -----------------------------------------------------------------------------------------------------------------------------------------
# def duplicar_impares(lista):
#     impares = []
#     for numero in lista:
#         operacion = numero % 2
#         if operacion != 0:
#             nueva_lista = numero * 2
#             impares.append(nueva_lista)
#     return impares
# resultado = duplicar_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(resultado)
#----------------------------------------------------------------------------------------------------------------------------------------
# Crea una función llamada solo_vocal_a(palabras). La función debe recibir una lista de palabras y devolver una nueva lista que contenga únicamente las palabras que comienzan con la letra "a" (minúscula).

# Entrada de ejemplo: ["manzana", "avion", "pera", "azul", "auto"]

# Resultado esperado: ["avion", "azul", "auto"]
# def solo_vocal_a(palabras):
#     lista_nueva = []
#     for palabra in palabras:
#         filtro = palabra[0]
#         if filtro == "a":
#             lista_nueva.append(palabra)
#     return(lista_nueva)
# resultado = solo_vocal_a(["manzana", "avion", "pera", "azul", "auto"])
# print(resultado)
#----------------------------------------------------------------------------------------------------------------------------------------
# Crea una función llamada filtrar_y_limitar(numeros). Debe recibir una lista de números y devolver una nueva lista que contenga solo los números que cumplan estas dos condiciones:

# Que el número sea par.

# Que el número sea mayor a 10.

# Entrada de ejemplo: [2, 12, 5, 20, 8, 30, 7]

# Resultado esperado: [12, 20, 30] (El 2 y el 8 son pares, pero no son mayores a 10, así que quedan fuera).

# def filtrar_y_limitar(numeros):
#     lista_filtrada = []
#     for numero in numeros:
#         if numero % 2 == 0 and numero >= 10:
#             lista_filtrada.append(numero)
#     return lista_filtrada

# resultado = filtrar_y_limitar([2, 12, 5, 20, 8, 30, 7])
# print(resultado)
#----------------------------------------------------------------------------------------------------------------------------------------
# Crea una función llamada contar_letras_i(lista_palabras). Debe recibir una lista de palabras y devolver un número entero que represente cuántas de esas palabras contienen la letra "i" (minúscula).

# Entrada: ["perro", "tigre", "gato", "bici"]

# Resultado esperado: 2 (porque "tigre" y "bici" tienen la "i").

# Tu "Caja de Herramientas":

# El Acumulador: Como quieres un número final, empieza con contador = 0.

# El Escáner: Para saber si una letra está dentro de una palabra, Python tiene una palabra mágica: in.

# Ejemplo: if "i" in palabra:

# El Proceso: Si la "i" está en la palabra, le sumas 1 al contador.

# Reto extra: Intenta hacerlo completamente solo. Piensa bien qué devuelves (return) y dónde lo pones. ¡Tú puedes!

# def contar_letras_i(lista_palabras):
#     contador_i = 0
#     for letra in lista_palabras:
#         if "i" in letra:
#             contador_i += 1 
#     return contador_i
    
# resultado = contar_letras_i(["avion", "casa", "tio", "carro", "manuel"])
# print(resultado)
#----------------------------------------------------------------------------------------------------------------------------------------
# Imagina que trabajas moderando un chat. Tienes una lista de palabras y quieres crear una nueva lista, pero si una palabra tiene más de 7 letras, es demasiado larga para el diseño del chat y debes sustituirla por el texto "LARGA". Las palabras cortas se quedan igual.

# Entrada: ["hola", "esternocleidomastoideo", "python", "programacion"]

# Resultado esperado: ["hola", "LARGA", "python", "LARGA"]

# Tu objetivo:
# Escribe la función censurar_palabras(lista).

# Reglas para este nivel:

# No te diré qué usar (¿if/else?, ¿append?, ¿len?).

# Si te da error, cópialo y pégalo aquí, pero intenta primero leer qué te dice Python.

# Si te quedas en blanco, dime: "estoy trabado", y solo entonces te daré una pista pequeña.

# ¡A por ello! Confío en que ya tienes las herramientas en la cabeza.

# def censurar_palabras(lista):
#     lista_nueva = []
#     for palabra in lista:
#         if len(palabra) >= 7:
#             lista_nueva.append("LARGA")
#         else:
#             lista_nueva.append(palabra)
#     return lista_nueva
# resultador = censurar_palabras(["hola", "esternocleidomastoideo", "python", "programacion"])
# print(resultador)
#----------------------------------------------------------------------------------------------------------------------------------------
# El Problema:
# Tienes una lista de invitados y una lista de personas que se portaron mal y tienen prohibida la entrada (la "lista negra"). Debes crear una función que devuelva una lista de los invitados que SÍ pueden pasar.

# La tarea:
# Escribe la función limpiar_invitados(invitados, lista_negra).

# Entrada:

# invitados: ["Luis", "Ana", "Pedro", "Marta"]

# lista_negra: ["Pedro", "Luis"]

# Resultado esperado: ["Ana", "Marta"]

# Un empujoncito filosófico (sin código):
# Para saber si alguien NO está en una lista, Python usa not in. Por ejemplo: if nombre not in lista_negra:.

# def lista_invitados(nombres, lista_negra):
#     invitados = []
#     for nombre in nombres:
#         if nombre not in lista_negra:
#             invitados.append(nombre)
#     return invitados
# resultado = lista_invitados(["Luis", "Ana", "Pedro", "Marta"], ["Pedro", "Luis"])
# print(resultado)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Escribe la función contar_vocales(texto). Debe recibir una cadena de texto y devolver el número total de vocales que contiene.

# Entrada de ejemplo: "murcielago"

# Resultado esperado: 5

# Reglas del juego:

# Sin pistas de estructura: Tú decides si usas total = 0, for, if, etc.

# Referencia: Necesitas saber qué es una vocal. Puedes crear una lista vocales = ["a", "e", "i", "o", "u"] dentro de tu función para comparar.

# El recorrido: Recuerda que si haces for letra in texto:, Python analizará cada letra por separado.

# def contar_vocales(palabra):
#     vocales_totales = 0 
#     vocales = ["a", "e", "i", "o", "u"]
#     for letra in palabra:
#         if letra.lower() in vocales:
#             vocales_totales += 1
#     return vocales_totales
# resultado = contar_vocales("HOla")
# print(resultado)
#----------------------------------------------------------------------------------------------------------------------------------------
# Crea una función llamada pedir_clave(). Dentro, debe usar un while que le pida al usuario una contraseña por teclado. Si la contraseña no es "python123", el bucle debe volver a pedirla. Si es correcta,

# def pedir_clave():
#     codigo = "python123"
#     clave = input("Por favor, ingrese la contrasena: ")
#     while clave != codigo:
#         print("Contrasena incorrecta")
#         clave = input("intentelo de nuevo: ")
#     print("Contrasena correcta, puede pasar.")

# pedir_clave()
#----------------------------------------------------------------------------------------------------------------------------------------
# Ahora que recordaste cómo evitar el bucle infinito, ¿podrías modificar la función para que el usuario solo tenga 3 intentos?

# Si falla 3 veces, el bucle debe terminar y decir: "Cuenta bloqueada por seguridad".

# Pista para tu lógica:

# Necesitas una variable nueva (un contador) que empiece en 0.

# Cada vez que el usuario falle, le sumas 1.

# Tu while ahora tendrá dos condiciones (puedes usar el and).

# def pedir_clave():
#     intentos = 0 
#     codigo = "phyton123"
#     clave = input("Por favor ingrese la clave: ")
#     while clave != codigo and intentos < 2:
#         print("Contrasena incorrecta")
#         intentos += 1
#         clave = input("Intentelo de nuevo: ")
#     print("Contrasena correcta, puede pasar")

# pedir_clave()
#---------------------------------------------------------------------------------------------------------------------------------------
# Imagina que eres el jefe de seguridad de un puerto. Tienes una lista de contenedores, donde cada contenedor es una lista de pesos de los paquetes que tiene dentro.

# Tu misión:
# Debes crear una función llamada procesar_puerto(contenedores).

# BUCLE FOR: Debes revisar cada contenedor de la lista.

# IF/ELSE:

# Si un paquete pesa más de 100 kg, es "PESADO".

# Si pesa 100 kg o menos, es "NORMAL".

# WHILE (El toque difícil): El sistema de escaneo es viejo y a veces falla. Antes de procesar cada contenedor, el programa debe pedirte una "Clave de Operador". No puede avanzar al siguiente contenedor hasta que pongas la clave correcta ("puerto77").

# def procesar_puerto(contenedores):
#     clave = "1234"
#     productos = ["producto 1", "producto 2", "producto 3"]
#     for contenedor in contenedores:
#         print(contenedor)
#         codigo = input("Por favor, ingrese la contrasena: ")
#         while codigo != clave:
#             print("Constrasena incorrecta")
#             codigo = input("Por favor, vuelva a intentarlo: ")
#         for producto in productos:
#             print(producto)
#             peso = int(input(f"Por favor, ingrese el peso de {producto}: "))
#             if peso >= 100:
#                 print("PESADO")
#             else:
#                 print("NORMAL")
# procesar_puerto(["Contenedor 1", "Contenedor 2", "Contenedor 3"])
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define la función cajero_automatico con los dos parámetros acordados.

# Inicia el bucle for para desempacar el nombre y la cantidad de la lista de listas.

# Dentro del for, abre un while que evalúe dos condiciones simultáneas: que el cliente necesite dinero y que el cajero tenga fondos.

# Dentro del while, realiza la operación matemática de resta (de 10 en 10) para ambas variables.

# Al salir del while (pero siguiendo dentro del for), usa un if para verificar si la cantidad del cliente llegó a 0 y muestra el mensaje correspondiente.

# Llama a la función al final pasando una lista de listas y un número para el efectivo

# def cajero_automatico(pedido_cliente, efectivo_cajero):
#     for cliente, pedido in pedido_cliente:
#         while pedido > 0 and efectivo_cajero > 10:
#             efectivo_cajero -= 10
#             pedido -= 10
#             print(f'{cliente} ha retirado 10$')

#         if pedido <= 0:
#             print(f'Retiro de {cliente} realizado con exito.')
#         else:
#             print(f'{cliente} el cajero ya no cuenta con fondos suficientes para completar su operacion.')

# cajero_automatico([["Sebastian", 100]], 95)
# #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def cajero_automatico(pedido_cliente, efectivo_cajero):
#     clientes_insatisfechos = []

#     for cliente, pedido in pedido_cliente:
#         while pedido > 0 and efectivo_cajero > 10:
#             efectivo_cajero -= 10
#             pedido -= 10
#             print(f'{cliente} ha retirado 10$')

#         if pedido <= 0:
#             print(f'Retiro de {cliente} realizado con exito.')
#         else:
#             print(f'{cliente} el cajero ya no cuenta con fondos suficientes para completar su operacion.')
#             clientes_insatisfechos.append(cliente)

#     return clientes_insatisfechos

# resultado = cajero_automatico([["Sebastian", 100], ["Fabian", 100]], 100)
# print(f'Lista de las personas que no lograron realizar su retiro {resultado}')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def nombre_barcos(barcos, energia_grua):
#     lista_pendientes = []
#     for barco in barcos:
#         nombre = barco[0]
#         contenedores = barco [1:]

#         for contenedor in contenedores:
#             if energia_grua >= contenedor:
#                 energia_grua -= contenedor
#                 print(f'Descargando contenedor de {contenedor}, del barco {nombre}.')
#             else:
#                 lista_pendientes.append(nombre)
#                 break

#     return lista_pendientes
# resultado = nombre_barcos([["la pinta", 20, 10], ["la nina", 5,10], ["la santa maria", 40, 50]], 100)
# print(resultado)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def entradas_vip(grupo_amigos, entradas_disponibles):
#     sin_entrada = []
#     for grupo in grupo_amigos:
#         nombre = grupo[0]
#         edades = grupo[1:]

#         for edad in edades:
#             if edad >= 18 and entradas_disponibles > 0:
#                 entradas_disponibles -= 1
#                 print(f'{nombre} recibe una entrada')
#             else:
#                 sin_entrada.append(nombre)
#                 break
    
#     return sin_entrada
# resultado = entradas_vip([["sexo", 18, 19, 20], ["ano", 25, 17, 14], ["malito", 18]], 10)
# print(resultado)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def cosecha(tipo_fruta):
#     fruta_recolectada = []

#     for fruta in tipo_fruta:
#         nombre = fruta[0]
#         calidades = fruta[1:]

#         for calidad in calidades:
#             if calidad == "madura":
#                 fruta_recolectada.append(nombre)
    
#     return fruta_recolectada
# resultado = cosecha([["Manzano", "madura", "verde", "madura"], ["Peral", "verde"], ["Ciruelo", "madura", "madura"]])
# print(resultado)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def procesar_cafeteria(pedidos, saldo_caja):

#     pedidos_pendientes = []
#     for pedido in pedidos:
#         if saldo_caja >= pedido["costo"]:
#             saldo_caja -= pedido["costo"]
#         else:
#             pedidos_pendientes.append(pedido["tipo"])
#             break
    
#     return(pedidos_pendientes)
# resultado = procesar_cafeteria([{"tipo": "Espresso", "costo": 5}, {"tipo": "Capuccino", "costo": 10}, {"tipo": "Latte Grande", "costo": 15}], 15)
# print(f'Los pedidos que quedaron sin procesar fueron: {resultado}')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# consolas = [
#         {"modelo": "PS5", "precio": 500, "stock": 2},
#         {"modelo": "Xbox", "precio": 400, "stock": 0},
#         {"modelo": "Switch", "precio": 300, "stock": 5}
#     ]

# def comprar_consolas(lista_consolas, presupuesto):
#     no_compradas = []

#     for consola in lista_consolas:
#         if presupuesto >= consola["precio"] and consola["stock"] > 0:
#             presupuesto -= consola["precio"]
#         else:
#             no_compradas.append(consola["modelo"])
#             break 
#     return no_compradas
# resultado = comprar_consolas(consolas, 400)
# print(resultado)

# inventario = [
#     {"modelo": "PS5", "precio": 500, "stock": 2},
#     {"modelo": "Xbox", "precio": 400, "stock": 0},
#     {"modelo": "Switch", "precio": 300, "stock": 5}
# ]

# def comprar_consolas (inventario, presupuesto, pedido):
#     no_compradas = []

#     for deseo in pedido:
        
#         for producto in inventario:

#             if producto["stock"] > 0 and deseo == producto["modelo"] and presupuesto >= producto["precio"]:
#                 presupuesto -= producto["precio"]
#                 pedido.remove(producto["modelo"])


#             else:
#                 if producto["modelo"] in pedido:
#                     no_compradas.append(producto["modelo"])
#                     producto["stock"] -= 1
#                     break

    
#     return no_compradas
# pedido = ["PS5", "PS5", "Xbox", "Switch", "Switch", "Switch"]

# resultado = comprar_consolas(inventario, 600, pedido)
# print(resultado)

# inventario = [
#     {"modelo": "PS5", "precio": 500, "stock": 2},
#     {"modelo": "Xbox", "precio": 400, "stock": 0},
#     {"modelo": "Switch", "precio": 300, "stock": 5}
# ]

# def comprar_consolas (inventario, presupuesto, pedido):
#     no_compradas = []

#     for deseo in pedido:

#         for producto in inventario:
#             if deseo == producto["modelo"]:

#                 if producto["stock"] > 0 and presupuesto > producto["precio"]:
#                     presupuesto -= producto["precio"]
#                 else:
#                     no_compradas.append(producto["modelo"])
#                 break
                    
#     return no_compradas
# pedido = ["PS5", "PS5", "Xbox", "Switch"]
# resultado = comprar_consolas(inventario, 600, pedido)
# print(resultado)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # TAREA 1
# menu = [
#     {"bebida": "Espresso", "precio": 2},
#     {"bebida": "Latte", "precio": 4},
#     {"bebida": "Capuccino", "precio": 5}
# ]
# def comprar_menu(menu, presupuesto, orden_cliente):
#     no_compradas = []

#     for pedido in orden_cliente:
       
#         for producto in menu:
#             if pedido == producto["bebida"]:

#                 if presupuesto >= producto["precio"]:
#                     presupuesto -= producto["precio"]
#                 else:
#                     no_compradas.append(producto["bebida"])
    
#     return no_compradas
# orden_cliente = ["Espresso", "Capuccino", "Latte"]
# resultado = comprar_menu(menu, 6, orden_cliente)
# print(resultado)
# #finalizado, cosas a preguntar: por que si coloco en if pedido == producto pero sin indicar ["bebida"] me da una lista al final de no compradas vacia, porque hay que senalizar

# # TAREA 2
# base_pasajeros = [
#         {"nombre": "Luis", "pasaporte_valido": True, "maleta_kilos": 20},
#         {"nombre": "Maria", "pasaporte_valido": False, "maleta_kilos": 15},
#         {"nombre": "Pedro", "pasaporte_valido": True, "maleta_kilos": 35}
#     ]
# prohibido_subir = []

# def avordaje_avion(base_pasajeros, fila_abordaje):
#     for persona in fila_abordaje:
        
#         for pasajero in base_pasajeros:
#             if persona == pasajero["nombre"]:

#                 if not pasajero["pasaporte_valido"] or pasajero["maleta_kilos"] > 23:    #AQUI TENIA <= 23
#                     prohibido_subir.append(pasajero["nombre"])

#     return prohibido_subir
# fila_abordaje = ["Luis", "Maria", "Pedro"]
# resultado = avordaje_avion(base_pasajeros, fila_abordaje)
# print(resultado)

# TAREA 3
# zonas_concierto = [
#         {"zona": "VIP", "precio": 150, "disponibles": 1},
#         {"zona": "General", "precio": 50, "disponibles": 10},
#         {"zona": "Gradas", "precio": 30, "disponibles": 0}
#     ]

# def comprar_entradas(zona_concierto, dinero_grupo, pedido_amigos):
#     no_compradas = []

#     for pedido in pedido_amigos:
#         for puesto in zona_concierto:

#             if pedido == puesto["zona"]:
                
#                 if dinero_grupo >= puesto["precio"] and puesto["disponibles"] > 0:
#                     dinero_grupo -= puesto["precio"]
#                     puesto["disponibles"] -= 1       #esta linea de codigo no la concidere 
#                 else:
#                     no_compradas.append(puesto["zona"])
    
#     return no_compradas
# pedido_amigos = ["VIP", "VIP", "Gradas", "General"]
# resultado = comprar_entradas(zonas_concierto, 220, pedido_amigos)
# print(resultado)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# catalogo_autos = [
#     {"marca": "Toyota", "precio": 20000, "unidades": 2},
#     {"marca": "Tesla", "precio": 40000, "unidades": 0},
#     {"marca": "Hyundai", "precio": 15000, "unidades": 5}
# ]

# def comprar_flota(presupuesto, pedido_cliente):
#     no_compradas = []
#     comprados = []      #agregado al final

#     for pedido in pedido_cliente:

#         #pedido = tesla
#         for coche in catalogo_autos:
#                 #pedido = tesla
#                 #cohce = toyota
                
#                 if pedido == coche["marca"]:
                    
#                     if presupuesto >= coche["precio"] and coche["unidades"] > 0:
#                         presupuesto -= coche["precio"]
#                         coche["unidades"] -= 1
#                         comprados.append(coche["marca"])
#                     else:

#                         if coche["unidades"] <= 0:
#                             no_compradas.append({"auto": coche["marca"], "motivo": "Sin unidades"})
#                         elif presupuesto < coche["precio"]:
#                             no_compradas.append({"auto": coche["marca"], "motivo": "Dinero insuficiente"})

#                 break     #por que es necesario utilizar un break aqui
                        
#     return no_compradas, comprados, presupuesto
# pedido_cliente = ["Tesla", "Tesla", "Hyundai"]
# coches_fallidos, coches_ok, dinero_restante = comprar_flota(20000, pedido_cliente)
# print("No comprados: ", coches_fallidos)
# print("Comprados: ", coches_ok) 
# print("Dinero restante: ", dinero_restante)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# catalogo_canciones = [
#     {"titulo": "Blinding Lights", "tamano_mb": 4, "premium": False},
#     {"titulo": "Bohemian Rhapsody", "tamano_mb": 12, "premium": True},
#     {"titulo": "Starboy", "tamano_mb": 5, "premium": False},
#     {"titulo": "Hotel California", "tamano_mb": 8, "premium": True}
# ]

# def descargar_playlist(espacio_disponible, usuario_premium, canciones_solicitadas):
#     rechazados = []
#     descargadas = []

#     for cancion in canciones_solicitadas:
#         for musica in catalogo_canciones:

#             if cancion == musica["titulo"]:

#                 if usuario_premium == True:
#                     if espacio_disponible >= musica["tamano_mb"]:
#                         espacio_disponible -= musica["tamano_mb"]
#                         descargadas.append(musica["titulo"])
#                     else:
#                         rechazados.append({"cancion": musica["titulo"], "motivo": "Espacio insuficiente"})
                
#                 else:
#                     if musica["premium"]:
#                         rechazados.append({"cancion": musica["titulo"], "motivo": "Requiere cuenta Premium"})
#                     elif espacio_disponible < musica["tamano_mb"]:
#                         rechazados.append({"cancion": musica["titulo"], "motivo": "Espacio insuficiente"})
#                     else:
#                         descargadas.append(musica["titulo"])
#                         espacio_disponible -= musica["tamano_mb"]

#     print(espacio_disponible)
#     return rechazados, descargadas, espacio_disponible

# canciones_solicitadas = ["Blinding Lights", "Bohemian Rhapsody"]
# canciones_rechazadas, canciones_descargadas, espacio_telefono = descargar_playlist(5, True, canciones_solicitadas)
# print("Canciones descargadas: ",canciones_descargadas)
# print("No se pudieron descargar: ", canciones_rechazadas)
# print("Espacio disponible: ", espacio_telefono)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fila_empleados = [
#     {"nombre": "Ana", "pase": 1, "destino": "Cafetería"},                                                                  
#     {"nombre": "Carlos", "pase": 1, "destino": "Servidores"},                                                  
#     {"nombre": "Elena", "pase": 5, "destino": "Presidencia"},                                                             
#     {"nombre": "Luis", "pase": 2, "destino": "Cafetería"}                                                                  
# ]
# zonas_empresa = [
#     {"area": "Cafetería", "nivel_requerido": 1, "presentes": 10, "capacidad_max": 12},
#     {"area": "Servidores", "nivel_requerido": 3, "presentes": 1, "capacidad_max": 2},
#     {"area": "Presidencia", "nivel_requerido": 5, "presentes": 0, "capacidad_max": 1}
# ]

# def control_acceso(fila_empleados, zonas_empresa):
#     exitosos = []
#     rechazados = []
    
#     for empleado in fila_empleados:

#         for zona in zonas_empresa:
#             if empleado["destino"] == zona["area"]:

#                 if empleado["pase"] >= zona["nivel_requerido"] and zona["presentes"] < zona["capacidad_max"]:
#                     exitosos.append(empleado["nombre"])
#                     zona["presentes"]+= 1
#                 else:
                    
#                     if empleado["pase"] < zona["nivel_requerido"]:
#                         rechazados.append({"Nombre":empleado["nombre"], "Motivo":  "Rango no permitido"})                    
#                     else:
#                         rechazados.append({"Nombre": empleado["nombre"], "motivo": "espacio insuficiente"})            
#                 break

                    
#     return exitosos, rechazados
# empleados_aceptados, empleados_rechazados = control_acceso(fila_empleados, zonas_empresa)
# print("Empleados aceptados", empleados_aceptados)
# print("Empleados rechazados", empleados_rechazados)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# inventario_hospital = [
#     {"zona": "Camas", "gravedad_minima": 1, "disponibles": 1},
#     {"zona": "Trauma", "gravedad_minima": 5, "disponibles": 2},
#     {"zona": "Quirofano", "gravedad_minima": 8, "disponibles": 0}
# ]
# fila_pacientes = [
#     {"nombre": "Andrés", "gravedad": 3, "necesita": "Camas"},
#     {"nombre": "María", "gravedad": 9, "necesita": "Quirofano"},
#     {"nombre": "Pedro", "gravedad": 2, "necesita": "Trauma"},
#     {"nombre": "Laura", "gravedad": 2, "necesita": "Camas"}
# ]
# def asignar_urgencias(fila_pacientes, inventario_hospital):
#     ingresados = []
#     rechazados = []
    
#     for paciente in fila_pacientes:
#         for zona in inventario_hospital:

#             if paciente["necesita"] == zona["zona"]:

#                 if paciente["gravedad"] >= zona["gravedad_minima"] and zona["disponibles"] > 0:
#                     ingresados.append(paciente["nombre"])
#                     zona["disponibles"] -= 1
#                 else:
#                     if paciente["gravedad"] < zona["gravedad_minima"]:
#                         rechazados.append({"Nombre" : paciente["nombre"], "Motivo": "Gravedad minima necesaria no registrada."})
#                     else:
#                         rechazados.append({"Nombre" : paciente["nombre"], "Motivo" : "Disponibilidad del area completada"})
            
#                 break

#     return ingresados, rechazados
# atendidos, no_atentidos = asignar_urgencias(fila_pacientes, inventario_hospital)
# print("Pacienten ingresados", atendidos)
# print("Pacientes sin atender", no_atentidos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
boxes = {
    "neumaticos": {"Blandos": 4, "Duros": 8, "Lluvia": 4},
    "mecanicos_disponibles": 6
}

autos_en_espera = [
    {"escuderia": "Ferrari", "pide": "Blandos", "mecanicos_necesarios": 4},
    {"escuderia": "Red Bull", "pide": "Blandos", "mecanicos_necesarios": 4},
    {"escuderia": "Mercedes", "pide": "Duros", "mecanicos_necesarios": 5},
    {"escuderia": "McLaren", "pide": "Lluvia", "mecanicos_necesarios": 8}
]

def gestionar_pit_stop(boxes, autos_en_espera):
    atendidos = []
    no_atendidos = []

    while len(autos_en_espera) > 0:
        auto = autos_en_espera.pop(0)
        
        if boxes["neumaticos"][auto["pide"]] >= 4 and auto["mecanicos_necesarios"] <= boxes["mecanicos_disponibles"]:
            boxes["neumaticos"][auto["pide"]] -= 4
            atendidos.append(auto["escuderia"])
        
        else:
            if auto["mecanicos_necesarios"] > boxes["mecanicos_disponibles"]:
                no_atendidos.append({"Escuderia": auto["escuderia"], "Motivo": "Mecanicos, no disponibles"})
            else:
                no_atendidos.append({"Escuderia": auto["escuderia"], "Motivo": "Neumaticos, no disponibles"})
    
    return atendidos, no_atendidos, boxes
atendidos, no_atendidos, boxes = gestionar_pit_stop(boxes, autos_en_espera)
print("atendidos", atendidos)
print("No atendidos", no_atendidos)
print(boxes)







  
                    

            

                    
                    



                

            
        