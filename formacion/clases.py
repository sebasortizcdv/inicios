# Introducción a la Programación Orientada a Objetos (POO)
#1)
# class Celular:
#     def __init__(self, marca, modelo, bateria_inicial):
#         self.marca = marca
#         self.modelo = modelo
#         self.bateria = bateria_inicial

#     def llamar(self, nombre_contacto):
#         return f"El {self.marca} {self.modelo} esta llamando a {nombre_contacto}"
    
#     def reproducir_video(self, nombre_video):
#         self.bateria -= 5
#         return f"El {self.modelo} de {self.marca}, esta reproduciendo {nombre_video}"

# mi_telefono = Celular("Apple", "IPhone 15", 100)
# tu_telefono = Celular("Samsung", "Galaxy S24",80)


# print(mi_telefono.marca)
# print(tu_telefono.marca)

# resultado = mi_telefono.reproducir_video("minecraft")

# print(resultado)
# print(f"El restante de la bateria es {mi_telefono.bateria}%")

# 2)
# class Coche:
#     def __init__ (self, marca, modelo, carga_maxima, velocidad_maxima):
    
#         self.marca = marca
#         self.modelo = modelo
#         self.carga_maxima = carga_maxima
#         self.velocidad_maxima = velocidad_maxima

#     def conducir(self, nombre_piloto):
#         return f"{nombre_piloto} esta condiciendo: {self.modelo}"

#     def abrir_puerta(self, nombre_persona, lado_puerta):
#         return f"{nombre_persona}, abrio el lado {lado_puerta}."
    
#     def estacionar_bajar_pasajero(self, nombre_piloto, nombre_pasajero):
#         print(f'El {self.modelo} se ha detenido por completo.')
#         accion_puerta = self.abrir_puerta(nombre_pasajero, "derecho")
#         return f"{accion_puerta} Mientras {nombre_piloto} apaga el coche"
         
#     def limitador_de_peso(self, peso_actual):
#         if self.carga_maxima < peso_actual:
#             return("Carga maxima superada, por favor, no superar la carga maxima permitida")
#         else:
#             return f"{self.modelo} lleva una carga de {peso_actual} pasajeros"
        
#     def limitador_de_velocidad(self, velocidad_actual, nombre_piloto):
#         if velocidad_actual > self.velocidad_maxima:
#             return ("Por favor, reducir la velocidad")
#         else:
#             return f"{self.modelo} es conducido por {nombre_piloto} a {velocidad_actual}"
    
# coche_1 = Coche("Hyundai", "Tucson", 4, 200)
# coche_2 = Coche("Ferrari", "La ferrari", 2, 300)

# resultado = coche_1.estacionar_bajar_pasajero("Sebastian", "Valeria")
# print(resultado)

#3)
# class Personaje:
#     def __init__(self, nombre, vida, energia, fuerza):

#         self.nombre = nombre
#         self.vida = vida
#         self.energia = energia 
#         self.fuerza = fuerza
#         self.esta_vivo = True 

#     def medidor(self):
#         return self.esta_vivo

#     def atacar(self, enemigo):
#             if not self.medidor():
#                 return f'{self.nombre} no puede atacar porque esta muerto'
            
#             return f'{self.nombre} ha atacado a {enemigo}, que pierde {self.fuerza} de vida'
        
    
#     def recibir_dano(self, dano):
#         if not self.medidor():
#                 return f'{self.nombre} ya esta muerto'
        
#         self.vida -= dano
#         if self.vida <= 0:
#             self.esta_vivo = False
#             return f'{self.nombre} esta MUERTO'
        
#         return f'{self.nombre} ha recibido {dano} puntos de da*o'

    
#     def meditar(self):
#         if not self.medidor():
#                 return f'{self.nombre} no puede meditar porque esta muerto'
        
#         self.energia += 15
#         resultado = self.energia
#         return f'Energia total: {resultado}'
    
#     def ataque_fulminante(self, enemigo):
#         if not self.medidor():
#                 return f'{self.nombre} no puede atacar porque esta muerto'
        
#         if self.energia >= 30:
#             self.energia -= 30
#             dano_especial = self.fuerza * 2
#             return f'{enemigo} ha recibido {dano_especial} de dan*o'
#         else:
#             print("No cuentas con los puntos de energia necesarios")
#             accion = self.meditar()
#             return f'{self.nombre} logro dar el golpe, pero antes tuvo que meditar. Energia actual {accion}'
            
        
# luffy = Personaje("luffy", 100, 30, 100)
# resultado = luffy.recibir_dano(100)
# print(resultado)

# 4)
# class Personaje:
#     def __init__(self, nombre, vida, fuerza, esta_vivo):
#         self.nombre = nombre
#         self.vida = vida
#         self.fuerza = fuerza
#         self.esta_vivo = esta_vivo

#     def medidor(self):
#         if self.vida <= 0:
#             self.esta_vivo = False
#         else:
#             self.esta_vivo = True
#         return self.esta_vivo
    
#     def dar_dano(self, enemigo):
#         enemigo.vida -= self.fuerza

#         if not enemigo.medidor():
#             enemigo.vida = 0
#             return f'{self.nombre} ha sido asesinado por {enemigo.nombre}.'
#         else:
#             return f'{enemigo.nombre} ha resistido. Le quedan {enemigo.vida} PS'

#     def atacar(self, enemigo):
#         if not self.medidor(): 
#             return (f'{self.nombre} esta muerto')

#         return self.dar_dano(enemigo)
        
#     def obtener_bono(self):
#         return 10
    
#     def calcular_fuerza_final(self):
#         resultado = self.fuerza + self.obtener_bono()
#         return resultado
    
#     def mostrar_poder(self):
#         return self.calcular_fuerza_final()
    
# personaje_1 = Personaje("luffy", 100, 50, True)
# personaje_2 = Personaje("Shanks", 100, 100, True)  

# print(personaje_1.atacar(personaje_2))

# 5)
# class Libro:
#     def __init__(self, nombre, autor, disponible):
#         self.nombre = nombre
#         self.autor = autor
#         self.disponible = disponible

#     def prestar(self, usuario):
#         if self.disponible:
#             self.disponible = False
#             return f'{self.nombre} ha sido prestado'
#         else:
#             return f'Lo siento {usuario.nombre}, {self.nombre} ya esta ocupado'
        
# class Usuario:
#     def __init__(self, nombre, tiene_libro):
#         self.nombre = nombre
#         self.tiene_libro = tiene_libro

#     def solicitar_libro(self, libro_solicitado):
#         if self.tiene_libro:
#             return f'{self.nombre}, Ya tienes un libro prestado, devuelve ese primero'
#         else:
#             respuesta = libro_solicitado.prestar(self)
#             self.tiene_libro = True
#             return respuesta

            
# libro_1 = Libro("El principito", "sebastian", False)
# usuario_1 = Usuario("Fabian", False)
# print(usuario_1.solicitar_libro(libro_1))

# 6)
# class Nave:
#     def __init__(self, modelo, combustible):
#         self.modelo = modelo
#         self.combustible = combustible
    
#     def viajar(self):
#         if self.combustible >= 20:
#             self.combustible -= 20
#             return f'Viaje EXITOSO. Combustible restante: {self.combustible} Lts'
#         else:
#             return f'ERROR. combustible insuficiente'
        
# class Plataforma:
#     def __init__(self, numero, ocupada):
#         self.numero = numero
#         self.ocupada = ocupada
        
#     def recibir_nave(self, nave_pasajera):
#         if self.ocupada:
#             return f'Plataforma {self.numero} ocupada'
#         else:
#             resultado = nave_pasajera.viajar()
            
#             if "ERROR" in resultado:
#                 return {resultado}
#             else:
#                 self.ocupada = True
#                 return f'{resultado}. Nave estacionada en plataforma {self.numero}'
        
# nave_1 = Nave("Machete", 15)
# plataforma_1 = Plataforma(1, False)

# print(plataforma_1.recibir_nave(nave_1))

# 6)
# class Producto():
#     def __init__(self, nombre_producto, precio_producto, stock):
#         self.nombre_producto = nombre_producto
#         self.precio_producto = precio_producto
#         self.stock = stock
#         self.exito = 0

#     def verificar_stock(self, cantidad_solicitada):
#         if self.stock >= cantidad_solicitada:
#             self.stock -= cantidad_solicitada
#             return {"estado": True, "mensaje": f'Has comprado {cantidad_solicitada} {self.nombre_producto}'}
        
#         elif self.stock > 0:
#             for _ in range (cantidad_solicitada):
#                 if self.stock > 0:
#                     self.stock -= 1
#                     self.exito += 1
#                 else:
#                     break
#             return {"estado" : True, "mensaje": f"STOCK insuficiente, cantidad comprada con exito: {self.exito}"}
     
#         else:
#             return {"estado" : False, "mensaje" :'Producto no disponible'}
        
# class Carrito():
#     def __init__(self, cantidad_deseada):
#         self.precio_total = 0
#         self.cantidad_deseada = cantidad_deseada

#     def comprar_productos(self, producto):
#         verificacion = producto.verificar_stock(self.cantidad_deseada)

#         if "STOCK" in verificacion["mensaje"]:
#             self.precio_total = producto.precio_producto * producto.exito
#             return f'{verificacion["mensaje"]}, PRECIO TOTAL {self.precio_total}$'
        
#         elif verificacion["estado"]:
#             self.precio_total = producto.precio_producto * self.cantidad_deseada
#             return f'{verificacion["mensaje"]}, PRECIO TOTAL {self.precio_total}$'

#         else:
#             return f'{verificacion["mensaje"]}'
        
# producto_1 = Producto("Playstation 5", 500, 5)
# carrito_1 = Carrito(4)
# print(carrito_1.comprar_productos(producto_1))

# 7)
# class Vehiculo:
#     def __init__(self, nombre, saldo_disponible):
#         self.nombre = nombre
#         self.saldo_disponible = saldo_disponible

# class Peaje:
#     def __init__(self, tarifa) :
#         self.recaudo = 0
#         self.rechazados = 0
#         self.aceptados = 0
#         self.tarifa = tarifa
        
#     def cobrar_peaje(self, vehiculo):
#         if vehiculo.saldo_disponible >= self.tarifa:
#             vehiculo.saldo_disponible -= self.tarifa
#             self.aceptados += 1
#             self.recaudo = self.recaudo + self.tarifa
#             return {"nombre": vehiculo.nombre, "Saldo restante": vehiculo.saldo_disponible, "Dinero acumulado": self.recaudo, "Aceptados": self.aceptados}
        
#         else:
#             self.rechazados += 1
#             return {"nombre": vehiculo.nombre, "Motivo": "Saldo insuficiente para el pago de la tarifa", "Rechazados": self.rechazados}

# coche = Vehiculo("Tucson", 60)

# peaje = Peaje(50)
# print(peaje.cobrar_peaje(coche))

# # 8)
# class Alarma:
#     def __init__(self, estado, modo):
#         self.estado = estado
#         self.modo = modo

#     def dar_mensaje(self):
#         if self.estado:
#             self.modo = "ALERTA"
#             return {"Estado de la alarma": self.modo, "Motivo": "Actividad sospechosa detectada"}
#         else:
#             return {"Estado de la alarma": self.modo, "Motivo": "Alarma desconectada"}
        

# class Sensor:
#     def __init__(self, movimiento):
#         self.movimiento = movimiento

#     def detectar_movimiento(self, alarma):
#         if self.movimiento:
#             return alarma.dar_mensaje()
            
#         else:
#             return {"Estado de la alarma": alarma.modo, "Motivo": "NO hubo movimiento"}
        
# alarma = Alarma(True, "ALERTA")
# sensor = Sensor(True)
# print(sensor.detectar_movimiento(alarma))

# # 9)
# class Cliente:
#     def __init__(self, nombre, salario, credito):
#         self.nombre = nombre
#         self.salario = salario
#         self.credito = credito

# class Evaluador:
#     def __init__(self):
#         self 
    
#     def evaluador_credito(self, cliente):
#         if cliente.salario >= 2000 and cliente.credito >= 70:
#             return {"Cliente": cliente.nombre, "Estado": "APROBADO"}
#         else:
#             if cliente.salario < 2000 and cliente.credito < 70:
#                 return f'{cliente.nombre} no cumple con ninguno de los requisitos para el credito'
            
#             elif cliente. salario < 2000:
#                 return {"Cliente": cliente.nombre, "Estado": "RECHAZADO", "Motivo": "Salario mensual insuficiente"}
            
#             elif cliente.credito < 70:
#                 return {"Cliente": cliente.nombre, "Estado": "RECHAZADO", "Motivo": "Historial crediticio no valido"}
            
# cliente = Cliente("Kellys", 20, 10)
# evaluador = Evaluador()
# print(evaluador.evaluador_credito(cliente))

# # 10)
# import random
# class Guerrero:
#     def __init__(self, nombre, vida, fuerza, defensa):
#         self.nombre = nombre
#         self.vida = vida
#         self.fuerza = fuerza
#         self.defensa = defensa
    
#     def pelea(self, enemigo):
#         numero_dado_1 = random.randint(1, 6)
#         self.fuerza += numero_dado_1
        
#         numero_dado_2 = random.randint(1, 6)
#         enemigo.fuerza += numero_dado_2

#         if self.fuerza > enemigo.fuerza:
#             enemigo.vida -= self.fuerza
            
#             return f'{self.nombre}, ha atacado a {enemigo.nombre} [{enemigo.vida} PS]'
        
#         else:
#             self.vida -= enemigo.fuerza

#             return f'{enemigo.nombre}, ha atacado a {self.nombre} [{self.vida} PS]'
        
# guerrero_1 = Guerrero("Luffy", 100, 70, 100)
# guerrero_2 = Guerrero("Shanks", 100, 70, 100)
# print(guerrero_1.pelea(guerrero_2))

# 11)
# class Cuenta_cliente:
#     def __init__(self, nombre_cliente, pin, saldo_disponible, saldo_retirar):
#         self.nombre_cliente = nombre_cliente
#         self.pin = pin
#         self.saldo_disponible = saldo_disponible
#         self.saldo_retirar = saldo_retirar

# class Cajero:
#     def __init__(self, saldo_disponible):
#         self.saldo_disponible = saldo_disponible
#         self.contrasena = 0
#         self.intentos = 0
    
#     def validar_pin(self, cliente):
#         while self.intentos < 3:
#             self.contrasena = int(input("Por favor, ingresar su PIN de seguridad:"))
#             if self.contrasena == cliente.pin:
#                 return True
#             self.intentos += 1 
#         return False

#     def retirar_dinero(self, cliente):
#         if self.validar_pin(cliente):

#             if self.saldo_disponible > 0:
#                 if cliente.saldo_disponible >= cliente.saldo_retirar:
#                     if self.saldo_disponible >= cliente.saldo_retirar:
#                         cliente.saldo_disponible -= cliente.saldo_retirar
#                         self.saldo_disponible -= cliente.saldo_retirar
#                         return {"Nombre": cliente.nombre_cliente, "Estado": "Retiro exitoso", "Saldo final": cliente.saldo_disponible}
#                     else:
#                         return {"Nombre": cliente.nombre_cliente, "Estado": "Cajero no cuenta con el saldo suficiente"}
#                 else:
#                     return {"Nombre": cliente.nombre_cliente, "Estado": f'{cliente.nombre_cliente} no cuenta con el saldo para realizar el retiro"'}
#             else:
#                 return "Sin plata mijo"
#         else:
#             return "Intentoos agotados"
        
# cajero = Cajero(60)
# cliente = Cuenta_cliente("sebastian", 1234, 2000, 50)
# print(cajero.retirar_dinero(cliente))

#12)
# class Materia_prima:
#     def __init__(self, lote):
#         self.lote = lote 

# class Maquina_industrial: 
#     def __init__(self, cantidad_ciclos):
#         self.cantidad_ciclos = cantidad_ciclos
#         self.ciclos = 0
#         self.realizadas = 0

#     def procesar_producto(self, producto):
#         while self.ciclos != self.cantidad_ciclos:
#             if producto.lote >= 3:
#                 producto.lote -= 3
#                 self.realizadas += 1 
#                 self.ciclos += 1
#             else:
#                 return {"Productos realizados": self.realizadas, "Material sin usar": producto.lote}
        
#         return {"Productos realizados": self.realizadas, "Material sin usar": producto.lote}
    
# producto = Materia_prima(20)
# maquina = Maquina_industrial(3)

# print(maquina.procesar_producto(producto))

# 13)
# simular la compra de pasajes. el avion tiene una cantidad de asientos disponibles.
# un pasajero quiere comprar una cantidad exacta de boletos y tiene un presupuesto exacto
# el boleto del avion tiene un precio fijo
 
# class Vuelo:
#     def __init__(self, asientos_disponibles):
#         self.asientos_disponibles = asientos_disponibles
#         self.precio_pasaje = 25

#     def comprar_boletos(self, pasajero):
#         if self.asientos_disponibles >= pasajero.asientos_comprar:
#             if pasajero.presupuesto >= self.precio_pasaje * pasajero.asientos_comprar:
#                 pasajero.presupuesto -= self.precio_pasaje * pasajero.asientos_comprar
#                 self.asientos_disponibles -= pasajero.asientos_comprar
#                 return {"Pasajero": pasajero.nombre, "Asientos comprados": pasajero.asientos_comprar}
#             else:
#                 return "No cuentas con el presupuesto mijo"
#         else:
#             if pasajero.presupuesto / self.precio_pasaje < pasajero.asientos_comprar:
#                 diferencia = pasajero.asientos_comprar - (pasajero.presupuesto / self.precio_pasaje)
#                 comprados = pasajero.asientos_comprar - int(diferencia)
#                 return {"Pasajero": pasajero.nombre, "Pasajes comprados": comprados}

# class Pasajero:
#     def __init__(self, nombre, presupuesto, asientos_comprar):
#         self.nombre = nombre
#         self.presupuesto = presupuesto
#         self.asientos_comprar = asientos_comprar


# vuelo = Vuelo(25)
# pasajero = Pasajero("Sebastian", 1000, 40)
# print(vuelo.comprar_boletos(pasajero))

# 14)

# class Vehiculo:
#     def __init__(self, placa, modelo):
#         self.placa = placa
#         self.modelo = modelo
        

# class Estacionamiento:
#     def __init__(self, capacidad):
#         self.capacidad = capacidad
#         self.lista_vehiculos = []

#     def verificar_puestos(self, lista_carros):
#         rechazados = 0

#         for carro in lista_carros:
#             if len(self.lista_vehiculos) < self.capacidad:
#                 self.lista_vehiculos.append(carro)
#             else:
#                 rechazados += 1

#         modelos_aceptados = [carro.modelo for carro in self.lista_vehiculos]

#         return {
#             "Autos estacionados": modelos_aceptados,
#             "Total adentro": len(self.lista_vehiculos),
#             "Autos rechazados": rechazados
#         }


# carro_1 = Vehiculo(1111, "ferrari")
# carro_2 = Vehiculo (2222, "fiesta")
# carro_3 = Vehiculo (3333, "machito")    

# carros = [carro_1, carro_2, carro_3]   

# estacionamiento = Estacionamiento(2)
# print(estacionamiento.verificar_puestos(carros))

# class Vehiculo:
#     def __init__(self, placa, modelo):
#         self.placa = placa
#         self.modelo = modelo
        

# class Estacionamiento:
#     def __init__(self, capacidad):
#         self.capacidad = capacidad
#         self.lista_vehiculos = []
#         self.rechazados = []

#     def verificar_puestos(self, coche):

#         if len(self.lista_vehiculos) < self.capacidad:
#             self.lista_vehiculos.append(coche)

#         else:
#             self.rechazados.append(coche)

#         coches_aceptados = [coche.modelo for coche in self.lista_vehiculos]
#         coches_rechazados = [coche.modelo for coche in self.rechazados]
            

#         return {
#             "Coches aceptados": coches_aceptados,
#             "Coches rechazados": coches_rechazados
#         }

# carro_1 = Vehiculo(1111, "ferrari")
# carro_2 = Vehiculo (2222, "fiesta")
# carro_3 = Vehiculo (3333, "machito")

# estacionamiento = Estacionamiento(1)

# print(estacionamiento.verificar_puestos(carro_1))
# print(estacionamiento.verificar_puestos(carro_2))
# print(estacionamiento.verificar_puestos(carro_3))# 

# 15)

# class Libro:
#     def __init__(self, titulo, autor):
#         self.titulo = titulo
#         self.autor = autor

# class Biblioteca:
#     def __init__(self):
#         self.libros_prestados = []
        
#         libro1 = Libro("El Quijote", "Cervantes")
#         libro2 = Libro("Python Pro", "Gomez")
        
#         self.libros_disponibles = [libro1, libro2]

#     def prestar_libro(self, libro):
#         for libro_disponible in self.libros_disponibles:
#             if libro.titulo == libro_disponible.titulo:
#                 self.libros_disponibles.remove(libro_disponible)
#                 self.libros_prestados.append(libro)
#             else:
#                 return "El libro que esta solicitando no se encuentra disponible"
            
#         libros_prestados = [libro.titulo for libro in self.libros_prestados]
        

#         return libros_prestados
    
# biblioteca = Biblioteca()
# libro_solicitado = Libro("El libro troll", "El rubius")

# print(biblioteca.prestar_libro(libro_solicitado))

# ENCAPSULACION DE CLASES (GETTERS Y SETTERS)
# 1) SIMULACION DE CAJA FUERTE, CON UN CODIGO O PIN, EL TIPO DE CONTENIDO QUE ALMACENA Y LOS INTENTOS FALLADOS AL ABRIRLA.

class Caja_fuerte:
    def __init__(self, codigo_pin, contenido):
        self.__codigo_pin = codigo_pin
        self.__contenido = contenido
        self.__estado = False
        self.__intentos_fallidos = 0

    def validar_pin(self, pin):
        if int(self.__codigo_pin) != pin:
            self.__intentos_fallidos += 1 
            print("Intento fallido, si recibes mucho fallos podrias bloquar la cuenta")

            if self.__intentos_fallidos == 3:
                self.set_nuevo_estado
                print("Tu cuenta ha sido bloqueada permanentemente.")
            return self.__intentos_fallidos
        
        else:
            if not self.__estado:
                return self.__contenido
            else:
                return "Tu cuenta ha sido bloqueada, desbloquear antes de intentar esta operacion."
    
    
    def set_nuevo_estado(self):
        self.__estado = True

    def get_estado(self):
        if self.__estado:
            print("Cuenta bloqueada")
        else:
            print("Cuenta activa")
    
    def set_codigo_pin(self, pin_nuevo):
        self.__codigo_pin = pin_nuevo


caja_fuerte = Caja_fuerte("1234", "dinero")

opcion = 0
import string
lista_minusculas = list(string.ascii_lowercase)

while opcion != 4:

    opcion = int(input("[1] Ver contenido\n[2] cambiar pin\n[3] Ver estado de la cuenta\n[4] salir\n[Tu respuesta]: "))
    if opcion == 1:
        pin = int(input("Por favor, ingrese si PIN: "))
        print(caja_fuerte.validar_pin(pin))

    if opcion == 2:
        nuevo_pin = input("Por favor, ingrese su nuevo PIN\n[Tu respuesta]: ")
        for letra in lista_minusculas:
            if letra in nuevo_pin:
                print("Tu PIN solo puede contener caracteres numericos.")
            else:
                if len(nuevo_pin) == 4:
                    caja_fuerte.set_codigo_pin(nuevo_pin)
                    print("Su PIN fue cambiado exitosamente.")
                else:
                    print("Su codigo debe ser de 4 digitos.")       

    if opcion == 3:
        caja_fuerte.get_estado()
        break

    if opcion == 4:
        break





    
    

        

                


