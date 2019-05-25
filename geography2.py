import random

diccionario ={"España": "Madrid", "Portugal": "Lisboa", "Francia": "Paris"}

for x in diccionario:
    #creamos una variable que nos generara un valor aleatorio dentro de el diccionario
    paises = random.choice(list(diccionario))
    #pedimos que se introduzca una respuesta a la pregunta y la guardamos en la variable respuesta
    respuesta = input(print("Cual es la capital de ",paises, "?"))
    #comparams la respuesta con el valor del diccionario correspondiente al pais que se ha generado aleatoriamente
    if respuesta == diccionario[paises]:
       print("La respuesta es correcta")
    else:
        while True:
            print("La respuesta es incorrecta, intentalo de nuevo:")
            pregunta = input(print("Cual es la capital de ", paises, "?"))
            if pregunta == diccionario[paises]:
                print("La respuesta es correcta")
                break
