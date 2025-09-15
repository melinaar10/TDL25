#Dado un listado de títulos de streams en Twitch,
# encuentre el título con más palabras y muéstrelo en pantalla.

titles = [
 "Speedrun de Super Mario en tiempo récord",
 "Charla sobre desarrollo de videojuegos",
 "Jugando al nuevo FPS del momento con amigos",
 "Música en vivo: improvisaciones al piano"
 ]

max_palabras=-1
streamMax= '''a'''

for elem in titles:
   if len(elem.split()) > max_palabras :
     max_palabras= len (elem.split())
     streamMax= elem

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#stream_max = max(titles, key=lambda t: len(t.split()))
#💡 Acá max() va recorriendo todos los títulos y usa len(t.split()) como criterio para decidir cuál es el “mayor”.

#lambda define una función anónima (sin nombre).
# En este caso, recibe un título t y devuelve len(t.split()).
# t.split() divide el título en una lista de palabras (separadas por espacios).
# len(...) devuelve la cantidad de palabras.

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print ("El título más largo es:", streamMax )