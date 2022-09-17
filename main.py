## TRIVIA SOBRE HISTOIRA DEL PERÚ
# IMPORTAMOS LAS LIBRERIAS
import time
import random
import pandas as pd

# GENERAMOS LAS CONSTANTES DE COLORES
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# MOSTRAMOS EL MENSAJE DE BIENVENIDA
print("*"*50)
print(GREEN +"Bienvenido a mi trivia sobre Historia del Perú"+RESET)
print(GREEN +"Pondremos a prueba tus conocimientos"+RESET)
print("*"*50)

print("\n")

print("Cargando", end="")
for i in range(0,5):
  time.sleep(1)
  print(".", end="")

print("\n")
# SOLICITAMOS EL NOMBRE Y EMPEZAMOS CON LA TRIVIA
nombre = input("Ingrese su nombre: ")

# PARA USAR EL WHILE LOOP para toda la trivia
iniciar_trivia = True  
intento = 0 

while iniciar_trivia == True: 
  intento += 1
  puntaje = 0
  
  print("\n")
  print(YELLOW+"*"*13)
  print("*INTENTO ", intento,"*")
  print("*"*13+RESET)
  print("\n")
  
  print("Escoje cualquier número siguiente: 10, 20, 30, 40")
  rang_superior = input("Ingresa algún número que se te ocurra :)  ")
  print("\n")
  while rang_superior not in ("10", "20", "30", "40"):
    rang_superior = input(RED+"Debes responder 10, 20, 30 o 40. Ingresa nuevamente tu respuesta: \n"+RESET)
    
  time.sleep(1)
  print("\n")
  print("Tu asignación de puntajes sera aleatoria y  tomara como base este número, suerte!!")
  time.sleep(3)
  puntaje = random.randint(0, int(rang_superior))
  
  print("\n")
  print("-"*50)
  print (GREEN+"Hola",nombre,", responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n"+RESET)
  print(GREEN+"Se te asigno", puntaje, "puntos. Suerte!!!"+RESET)
  print("-"*50)

  puntaje2    = []
  descripcion = []
  
  puntaje2.append(puntaje)
  descripcion.append("Puntaje de partida")
  
  print("\nCargando", end="")
  for i in range(0,5):
    time.sleep(1)
    print(".", end="")
  
  # COMENZAMOS CON LA TRIVIA
  
  print("\n")
  time.sleep(3)
  
  # PREGUNTA 01
  print (CYAN+"1) ¿En qué año fue el combate de 2 de mayo?"+RESET)
  alternativas = ["a)", "b)", "c)", "d)"]
  respuestas = ["1821", "1844", "1866", "1824"]

  for i in range(0, 4):
    print(alternativas[i], respuestas[i])
  
  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \n"+RESET)
  
  if respuesta_1 == "a":
    puntaje -= random.randint(0, 5)
    print("\nIncorrecto!", nombre, "ese año fue la independencia del Perú :)")
    print(nombre, "llevas", puntaje, "puntos")
    
  elif respuesta_1 == "b":
    puntaje -= random.randint(0, 5)
    print("\nCerca! pero equivocado", nombre, "este año en nuestro país ocurrio lo que se llamo <<La revolución de Arequipa de 1844>> más información https://es.wikipedia.org/wiki/Guerra_civil_peruana_de_1843-1844 ;)")
    print(nombre, "llevas", puntaje, "puntos")
  
  elif respuesta_1 == "d":
    puntaje -=random.randint(3, 8)
    print("\nIncorrecto! y por mucho", nombre, "este año en nuestro país se dio la <<La batalla de Ayacucho>>")
    print(nombre, "llevas", puntaje, "puntos")
  
  else:
    puntaje += random.randint(5, 10)
    print("\nRespuesta correcta, muy bien!!")
    print(nombre, "llevas", puntaje, "puntos")

  puntaje2.append(puntaje)
  descripcion.append("1ra pregunta")
  
  print("\n")
  time.sleep(3)
  
  # SEGUNDA PREGUNTA  
  print("-"*15)
  print (CYAN+"2) ¿En qué año fue la guerra con Chile?"+RESET)

  alternativas = ["a)", "b)", "c)", "d)"]
  respuestas   = ["1878", "1879", "1880", "1885"]

  for i in range(0,4):
    print(alternativas[i], respuestas[i])
  
  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \n"+RESET)
  
  if respuesta_1 == "a":
    puntaje -=random.randint(0, 5)
    print("\nIncorrecto! pero cerca", nombre, "en este año estamos a poco de la respuesta")
    print(nombre, "llevas", puntaje, "puntos")
  
  elif respuesta_1 == "c":
    puntaje -=random.randint(0, 5)
    print("\nIncorrecto! pero cerca", nombre, "en este año estamos a poco de la respuesta")
    print(nombre, "llevas", puntaje, "puntos")
  
  elif respuesta_1 == "d":
    puntaje -=random.randint(4, 8)
    print("\nIncorrecto!", nombre, "por poco y nos indicas el año que termino la guerra jejejeje")
    print(nombre, "llevas", puntaje, "puntos")
    
  else:
    puntaje +=random.randint(5, 10)
    print("\nRespuesta correcta, muy bien!!")
    print(nombre, "llevas", puntaje, "puntos")

  puntaje2.append(puntaje)
  descripcion.append("2da pregunta")
  
  print("\n")
  time.sleep(3)
  
  # TERCERA PREGUNTA
  print("-"*15)
  print (CYAN+"3) ¿Quién fue el héroe en la batalla de Arica"+RESET)

  alternativas = ["a)", "b)", "c)", "d)"]
  respuestas   = ["Francisco Pizarro", "Francisco Bolognesi", "Diego de Almagro", "Andres Avelino Caceres"]
  
  for i in range(0, 4):
    print(alternativas[i], respuestas[i])
  
  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \n"+RESET)
  
  if respuesta_1 == "a":
    puntaje =puntaje/2
    print("\nIncorrecto!", nombre, "el fue uno de los conquistadores :|")
    print(nombre, "llevas", puntaje, "puntos")
    print("\n")
  
  elif respuesta_1 == "c":
    puntaje =puntaje-10
    print("\nIncorrecto!", nombre, "el fue uno de los conquistadores :|")
    print(nombre, "llevas", puntaje, "puntos")
    print("\n")
  
  elif respuesta_1 == "d": 
    puntaje = puntaje*2
    print("\nEquivocado! pero cerca", nombre, "para recordarlo mucho más rapido, el fue llamado <<el brujo de los andes>>")
    print(nombre, "llevas", puntaje, "puntos")
    print("\n")
    
  else:
    puntaje +=300
    print("\n")
    print("¡¡INCORRECTO!! tan mal no podemos estar")
    print("\n")
    time.sleep(4)
    print(":V :V :V :V :V")
    print("jejejejeje")
    time.sleep(2)
    print("\n")
    print("Respuesta correcta, muy bien!!")
    print("Por esta pregunta ganaste <<300 PUNTOS!!>>")
    print("\n")
    print(nombre, "llevas", puntaje, "puntos")
    print("\n")
  
  time.sleep(2)

  puntaje2.append(puntaje)
  descripcion.append("3ra pregunta")
  print(CYAN+"EVOLUCIÓN DE TU PUNTAJE"+RESET)
  score = pd.DataFrame({'Descripción': descripcion,
                       'Evolucion del puntaje'    : puntaje2})
  print(score)
  
  print("\nHasta el momento tienes ", puntaje, "puntos\n")

  time.sleep(2)
  
  print(" -"*30)
  print(GREEN+"¿Deseas probar suerte para incrementar aleatoriamente tu puntaje?"+RESET)
  print(GREEN+"Puedes hacerlo las veces que quieras, hasta que indiques finalizar"+RESET)
  print(" -"*30)
  print("\n")
  
  iniciar_ruleta = True
  intentos = 0 
  while iniciar_ruleta == True:
    intentos +=1
    repetir_ruleta = input(CYAN+"Ingresa 'si' para repetir, o cualquier tecla para finalizar: \n>"+RESET).lower()
    print("Intento N°", intentos)
    print("Calculando...")
    time.sleep(2)
    puntaje = puntaje+random.randint(10, 30)
    print("Tu puntaje aumento a: ", puntaje, "\n")
  
    if repetir_ruleta != "si":
      print(nombre, "Espero que te haya ayudado a incrementar tu puntaje")
      iniciar_ruleta = False
  
  print("\n")
  print(RED+"-"*65)
  print(">>  Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos")
  print("-"*65+RESET)

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si": 
   print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  