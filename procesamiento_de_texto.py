#Procesar el archivo y extraer:
#Cantidad de vocales
#cantidad de consonantes
#Listado de las 50 palabras que más se repiten

file = open('archivo.txt') #Abre el archivo.
texto = file.read() #Lee el contenido del archivo y lo guarda en la variable 'texto'.

#Lista de vocales y lista de consonantes en minúscula y mayúscula.
vocales=["a","e","i","o","u","A","E","I","O","U"]
consonantes=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]

#Inicializa contadores de vocales (V) y consonantes (C).
V=0
C=0

for letra in texto: #Itera sobre cada carácter del texto.
    if letra in vocales: #Si el carácter está en la lista de 'vocales' incrememta 1 al valor de V.
        V+=1
    elif letra in consonantes: #Si el carácter está en la lista de 'consonantes' incrememta 1 al valor de C.
        C+=1

#Imprime el número de vocales y consonantes.
print(f"El número de vocales es: {V}")
print(f"El número de consonantes es: {C}")

#Lista de símbolos que se van a eliminar del texto.
simbolos = "|!\"#$%&/()=?'+*~[]^,;.:-_@\n\t<>" 

#Reemplaza cada símbolo de la lista en el texto por un espacio (" ").
for caracter in simbolos:
    texto = texto.replace(caracter," ")

texto = texto.lower() #Convierte todas las letras del texto a minúsculas.
palabras = texto.split(" ") #Divide el texto en una lista de palabras, usando como criterio de separación el espacio (" ").

#Por medio de una list comprehension, se añaden a la lista 'palabras' solo aquellas palabras que no están vacías.
palabras = [palabra for palabra in palabras if (palabra!='') ]  

frecuencia_palabras = {} #Diccionario para almacenar cada palabra junto a su frecuencia.

for palabra in palabras: #Itera sobre cada palabra en la lista 'palabras'.
    if palabra in frecuencia_palabras: #Verifica si la palabra ya existe en el diccionario.
        frecuencia_palabras[palabra]+=1 #Si la palabra ya existe, se incrementa el valor de su frecuencia en 1.
    else: #Si la palabra no existe en el diccionario.
        frecuencia_palabras[palabra] = 1 #Agrega la palabra al diccionario como clave y como valor se establece una frecuencia inicial de 1.

#Ordena los elementos del diccionario con la función sorted().
#Se especifica que se va a ordenar la lista de tuplas 'frecuencia.palabras'.
#Se especifica que se debe ordenar según el segundo elemento de cada tupla, es decir la frecuencia.
#Se indica que se deben ordenar los elementos de mayor a menor.
palabras_ordenadas = sorted(frecuencia_palabras.items(), key=lambda item: item[1], reverse=True)

# Imprime las 50 palabras que más se repiten junto con su frecuencia.
print("Las 50 palabras que más se repiten en el texto son:")
for palabra, frecuencia in palabras_ordenadas[:50]: # Itera sobre las primeras 50 tuplas de 'palabras_ordenadas'.
    print(f"{palabra} -> {frecuencia}")