diccionario ={"España": "Madrid", "Portugal": "Lisboa", "Francia": "Paris"}
#creamos un bucle que recorra las claves y valores del diccionario a la vez y vamos guardando cada pasado
#la clave en pais, y el valor en ciudad
for pais, ciudad in diccionario.items():
    respuesta = input(print("Cual es la capital de ", pais, "?"))
    #si la respuesta que pedimos por input, coincide con la ciudad, se lo hacemos saber al jugador y pasamos a la siguiente pregunta
    if respuesta == ciudad and pais != "Francia":
        print("Has acertado!, Pasemos a la siguiente pregunta: ")
    elif respuesta == ciudad and pais == "Francia":
        print("Enhorabuena has acertado todas las capitales, adios")
    #si no ha acertado, le decimos que se ha equivocado y entramos en un bucle para que repita la pregunta hasta que la acierte
    else:
        while True:
            print("La respuesta es incorrecta, intentalo de nuevo:")
            respuesta = input(print("Cual es la capital de ", pais, "?"))
            if respuesta == ciudad:
                if pais != "Francia":
                    print("has acertado!, Pasemos a la siguiente pregunta:")
                    break
                else:
                    print("Enhorabena, has acertado todas las capitales, adios")
                    break
