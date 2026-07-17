status="playing football"
print(status)

status="la mama tuya"
print(status)

print("jon"+"athan")
mitad_de_nombre="jon"
print(mitad_de_nombre+"athan")
print("athan"+mitad_de_nombre)

nombre="sebastian"

apellido="ortiz"
print(nombre+" "+apellido)

titulo="Ms. "
nombre="Irene"
print(titulo+nombre)


numero_de_aplicaciones=7+2
print(numero_de_aplicaciones)

percet=0.5*100
print(percet)

numero_de_pasos=100
print(numero_de_pasos+1)

numero_de_pasos=100
print(numero_de_pasos)
print("Genial!")

numero_de_pasos=80
print("estan por el buen camino, tu total es: "+str(numero_de_pasos+80))

print(f'estan por el buen camino, tu total es: {numero_de_pasos+80}')

numero = 2

print(f'este es el numero que buscas: {numero}')

nombre="sebastian"
print(len(nombre))

nombre="sebastian"
print(nombre)
print("Ahora lo deletreare")
for letra in nombre:
    print(letra)

private=3
public=10
print(f'total posts:{private+public}')

niños=5
niñas=10
total=niños+niñas
print(total)
print(f'total de niños y niñas es: {total}')

nombre = 'sebastian'
familia=4
print(f'la familia de {nombre} es de un total de {familia} personas')

#1era tarea (lista de edades)
#Realizar una lista de edades, iterar cada edad y en el proceso de iteracion comprobar si esa edad en cuestion es mayor o menor de edad, en caso de ser menor de edad debe imprimir en pantalla ("la edad es de:***, es menor de edad" y viceversa)

edades=[18,19,20,40,25,22,25,17,15,26,18,19,22,20,9,7,5,6,3,7,8]
for edad in edades:
    if edad >= 18:
       print(f'la edad es de: {edad}, es mayor de edad')
    else:
        print(f'la edad es de: {edad}, es menor de edad')

#2da tarea (lista de nombres)
#realizar una lista de nombres, donde iteres y evalues la cantidad de letras que tiene, si tiene mas de 5 debe imprimir "AZUL" y caso contrario imprimir ROJO

lista_de_nombres=["sebastian","fabian","jose","maria","ana","pedro","luis","josefina","cristina","diosdado"]
for nombre in lista_de_nombres:
   if len(nombre)>5:
       print(f'el nombre {nombre} es de color AZUL')
   else:
        print(f'el nombre {nombre} es de color ROJO')

#3ra tarea El Saludo Personalizado
#Objetivo: Practicar la entrada (input) y salida (print) de datos.
#La tarea: Crea un programa que le pregunte al usuario su nombre y luego lo salude de forma amistosa.
#Ejemplo de resultado: Hola Sebastián, ¡bienvenido al mundo de Python!

nombre=(input("Por favor, ingresa tu nombre: "))
print(f"Hola {nombre}, bienvenido al mundo de Python!")

#4ta tarea. Calculadora de edad

nombre=(input("Porfavor, ingresa tu nombre:"))
current_year=input("ingresar la fecha de hoy: ")
birth_year=input("Ingresar tu fecha de nacimiento: ")
print(f'Hola {nombre} tu edad es: {int(current_year)-int(birth_year)} años')

#5ta tarea. El Validador de Fiesta
#Objetivo: Usar condicionales simples (if / else).
#La tarea: Pregunta al usuario su edad. Si tiene 18 años o más, imprime "Puedes pasar a la fiesta". Si tiene menos de 18, imprime "Lo siento, te vas a casa".

edad= int(input("Porfavor, ingresa tu edad: "))
if edad >= 18:
    print("Feicidades!, puedes entrar a la isla de epstein")
else:
    print("Te perdiste de la vaina buena primo")

#6ta tarea. 
# Convertidor de GradosObjetivo: Aplicar una fórmula matemática básica.La tarea: Crea un programa que convierta grados Celsius a Fahrenheit.Fórmula: $F = (C \times 9/5) + 32 (Instrucciones: Pide los grados Celsius al usuario, realiza la operación y muestra el resultado final.)

celcius=int(input("Por favor, ingresar la temperatura local: "))
resultado = (celcius*9/5)+32
print(f'El resultado del calculo es {resultado}°F')
if resultado >= 62:
    print("Coño papi, tu estas es bello")
else:
    print("Uste esta cagando cubito mi hermano")



   

    