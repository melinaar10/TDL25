import random
import sys  # para poder usar sys.exit()

puntaje = 0

# Preguntas, respuestas y sus correctas
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

correct_answers_index = [1, 2, 0, 3, 1]

# Unimos las 3 listas en una sola y elegimos 3 preguntas al azar
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for question, options, correct_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
            # Verificamos si el número está dentro del rango
            if user_answer < 0 or user_answer >= len(options):
                print("Respuesta no válida")
                sys.exit(1)
        except ValueError:
            print("Respuesta no válida")
            sys.exit(1)

        # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
            puntaje += 1
            print("¡Correcto!")
            break
        else:
            if intento == 1:  # Si se acabaron los intentos
                print("Incorrecto. La respuesta correcta es:")
                print(options[correct_index])
            else:
                puntaje -= 0.5
                print("Incorrecto, intenta nuevamente.")

    print()  # Salto de línea después de cada pregunta

print("FINAL DEL JUEGO. PUNTAJE:", puntaje)


#Cambios importantes:
#Usamos zip(questions, answers, correct_answers_index) para agrupar todo en una sola lista de tuplas.
#Cada tupla es de la forma (pregunta, opciones, indice_correcto).
#random.choices(..., k=3) selecciona 3 preguntas al azar.
#Ya no accedemos por índices (questions[i], answers[i], etc.), sino que directamente usamos las variables question, options y correct_index.

#1. zip(questions, answers, correct_answers_index)
#🔗 Une las tres listas en una sola secuencia de tuplas.
#Cada tupla es de la forma:
#  ("pregunta", ("opciones..."), indice_correcto)

#2. list(...)
#Convierte ese objeto zip en una lista “real” que Python puede manejar más fácilmente.

#3. random.choices(..., k=3)
#Elige 3 elementos al azar de esa lista.
#El resultado es otra lista, pero solo con 3 tuplas seleccionadas.

#ntonces, questions_to_ask termina siendo una lista de 3 preguntas con sus opciones y la respuesta correcta,
#  que después vos vas recorriendo con:
#for question, options, correct_index in questions_to_ask:
#⚠️ Detalle: random.choices puede repetir preguntas.
#Si querés que no repita, hay que usar random.sample en lugar de choices.

#🔹 random.choices(population, k=N)
#Sirve para elegir varios elementos (con repetición permitida).
#Parámetros:
# population: la lista/tupla/etc. de donde se eligen los elementos.
# k: cuántos elementos queremos.