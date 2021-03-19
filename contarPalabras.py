import os

texto = 'este es un texto el cual deben contar el numero de palabras que tiene, deben tener en cuenta, que algunas palabras se separa por un punto, y una coma, tambien hay que tener en cuenta, que las palabras escritas EN MAYUSCULAS y minusculas cuenta como una este. Texto'

listaPalabras = texto.split()

contarPalabras = []
for palabra in listaPalabras:
    contarPalabras.append(listaPalabras.count(palabra))
    lista = set(listaPalabras)


os.system ("cls")
print("Texto:\n" + texto +"\n")
print("Número de veces que aparace una palabra:\n" + str(sorted(list(zip(lista, contarPalabras)))))
