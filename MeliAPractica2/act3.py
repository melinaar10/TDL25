
#Dado un código de conducta para un servidor de Discord.
# Solicite una palabra clave al usuario e imprima todas las reglas que la contengan

rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
 Evita el spam. No publiques enlaces sospechosos o repetitivos.
 No compartas información personal.
 Usa los canales adecuados para cada tema.
 Sigue las instrucciones de los moderadores."""

palabra = input("Ingresa una palabra: ")

for line in rules.splitlines():   # recorro cada regla (línea)
    words = line.split()          # separo en palabras
    for w in words:               # recorro palabra por palabra
        if w.lower() == palabra.lower():   # comparación exacta, ignorando mayúsculas
            print(line)
            break   # si ya encontré la palabra en la línea, no sigo revisando
 
 #///////////////////////////////////////////////////////////////////////////////////////////////////////
 # EFICIENTE
palabra = input("Ingresa una palabra: ")

for line in rules.splitlines():
    if palabra.lower() in line.lower():
        print(line)


