import resultados_icfes as logic
import pandas as pd
from pandas import DataFrame

def ejecutar_cargar_datos()->DataFrame:

    """
    
    Solicita al usuario que ingrese el nombre de un archivo
    CSV con los datos estadisticos de la prueba ICFES Saber
    11. sin la extension.
    
    Retorno: DataFrame
        Informacion del archivo CSV leida como DataFrame.

    """

    data = None
    archivo = input("Por favor ingrese el nombre del archivo CSV, sin extension: ")
    data = logic.cargar_datos("./" +  archivo + ".csv")
    if len(data)==0:
        print("El archivo seleccionado no es válido. No se pudo cargar la información.")
    else:
        print("\nSe cargo el archivo correctamente.")

    
    return data

def ejecutar_distribucion_nacionalidad(datos:DataFrame):

    """

    Ejecuta la opcion de consultar la distribucion de
    nacionalidad entre los evaluados.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        Retorna una grafica de barras verticales con la
        informacion solcitada.

    """

    print(logic.distribucion_nacionalidad(datos))

def ejecutar_distribucion_genero_estrato(datos:DataFrame):

    """

    Pide al usuario un numero de estrato entre 1 y 6 y
    ejecuta la opcion de consultar los porcentajes de genero
    entre los evaluados pertenecientes a ese estrato.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        Retorna una grafica de torta con la informacion
        solcitada.

    """

    validez = False
    estrato = ""
    while validez == False:
        estrato_numero = int(input("Ingrese un estrato. Valor de 1 a 6: "))
        estrato = f"Estrato {estrato_numero}"
        if estrato_numero < 1 or estrato_numero > 6:
            print("El estrato ingresado no es valido.")
        else:
            validez = True
            print(logic.distribucion_genero_estrato(datos, estrato))

def ejecutar_desempeño_departamentos(datos:DataFrame):

    """

    Ejecuta la opcion de consultar los 10 mejores
    departamentos tomando como criterio el promedio del 
    puntaje global de todos los evaluados que pertenecen a
    ese departamento.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        Retorna una grafica de barras horizontales
        con los departamentos y sus respectivos puntajes globales promedio.

    """

    print(logic.desempeño_departamentos(datos))

def ejecutar_municipio_puntajes_bajo(datos:DataFrame):

    """

    Solicita al ususario el departamento con el que desea
    consultar la informacion y ejecuta la opcion de consultar
    los peores 5 municipios del departamento dado por el
    usuario tomando como criterio el promedio del puntaje
    global de todos los evaluados que pertenecen a ese
    departamento.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        Retorna una grafica de barras hotizontales con la
        informacion solicitada y con los respectivos puntajes
        de cada una de las areas evaluadas de los respectivos
        municipios tomando como criterio el promedio en cada
        una de las areas de todos los evaluados que pertenecen
        a ese municipio.

    """

    departamentos = datos.loc[:, "DEPARTAMENTO"].unique()
    validez = False
    while validez == False:
        departamento = (input("Ingrese el departamento del que desea saber la informacion: ")).upper()
        if departamento in departamentos:
            validez = True
            print(logic.municipio_puntajes_bajo(datos, departamento))
        else:
            print("El departamento ingresado no es valido.")

def ejecutar_desempeño_municipio_categoria(datos:DataFrame):

    """

    Solicita al ususario una area de evaluacion y ejecuta la
    opcion de consultar los mejores 10 municipios en esa area
    tomando como criterio el desempeño promedio de los
    evaluados pertenecientes a cada municipio en la area
    evaluada.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        Retorna una grafica de barras horizontales con la informacion solcitada y el
        promedio de cada municipio en la area solicitada.

    """

    validez = False
    print("\n1. Matematicas\n2.Lectura Critica\n3.Ingles\n4.Ciencias sociales\n5.Naturales")
    while validez == False:
        categoria = int((input("Ingrese el indice del area de la cual quiere saber la informacion: ")))
        if categoria == 1:
            validez = True
            categoria = -5
            materia = "matematicas"
            print(logic.desempeño_municipio_categoria(datos, categoria, materia))
        elif categoria == 2:
            validez = True
            categoria = -6
            materia = "lectura critica"
            print(logic.desempeño_municipio_categoria(datos, categoria, materia))
        elif categoria == 3:
            validez = True
            categoria = -2
            materia = "ingles"
            print(logic.desempeño_municipio_categoria(datos, categoria, materia))
        elif categoria == 4:
            validez = True
            categoria = -3
            materia = "ciencias sociales"
            print(logic.desempeño_municipio_categoria(datos, categoria, materia))
        elif categoria == 5:
            validez = True
            categoria = -4
            materia = "ciencias naturales"
            print(logic.desempeño_municipio_categoria(datos, categoria, materia))
        else:
            print("El indice evaluacion ingresado no es valido.")

def ejecutar_desempeño_estratos(datos:DataFrame):

    """

    Ejecuta la opcion de consultar el desempeño de cada uno de
    los estratos tomando como criterio el desempeño promedio
    de los evaluados pertenecientes a cada estrato.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        Retorna una diagrama de bigotes con la informacion
        solcitada.

    """

    print(logic.desempenio_estratos(datos))

def ejecutar_relacion_nutricion_desempenio(datos:DataFrame):
    
    """

    Solicita al ususario el indice de una area de
    evaluacion y el indice de algun grupo alimenticio con
    respecto al menu mostrado y ejecuta la opcion de
    relacionar el desempeño de las personas en la area
    de evaluacion insertada por el usuario, tomando como 
    cirterio el promedio entre todos los puntajes globales
    de las personas que consumen alimentos del grupo
    alimenticio dado por el ususario, con la frecuencia que
    esas personas consumen alimentos del grupo alimenticio
    dado por el usuario.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        Retorna un diagrama de bigotes con la informacion
        solcitada.

    """

    print("\nAreas:\t\t\tGrupos alimenticios:\n1. Ciencias naturales\t1. Proteinas\n2. Ciencias sociales\t2. Lacteos\n3. Matematicas\t\t3. Frutos\n4. Lectura critica\n5. Ingles\n")
    
    validez = False

    while validez == False:
        categoria = int(input("Ingrese el indice del area de la prueba que desea relacionar: "))
        if categoria == 1:
            validez = True
            categoria = "PUNT_NATURALES"
        elif categoria == 2:
            validez = True
            categoria = "PUNT_SOCIALES"
        elif categoria == 3:
            validez = True
            categoria = "PUNT_MATEMATICAS"
        elif categoria == 4:
            validez = True
            categoria = "PUNT_LECTURA_CRITICA"
        elif categoria == 5:
            validez = True
            categoria = "PUNT_INGLES"
        else:
            print("El indice ingresado no es valido.")
    
    validez = False

    while validez == False:
        grupo_alimenticio = int(input("Ingrese indice del grupo alimenticio que desea relacionar: "))
        if grupo_alimenticio == 1:
            validez = True
            grupo_alimenticio = "PROTEINAS"
        elif grupo_alimenticio == 2:
            validez = True
            grupo_alimenticio = "LACTEOS"
        elif grupo_alimenticio == 3:
            validez = True
            grupo_alimenticio = "FRUTOS"
        else:
            print("El indice ingresado no es valido.")

    print(logic.relacion_nutricion_desempenio(datos, grupo_alimenticio, categoria))

def ejecutar_crear_matriz(datos:DataFrame):

    """

    Ejecuta la opcion de crear una matriz.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        tupla: tuple
            Tupla de 3 elementos los cuales son:  matriz que cruza
            los estratos de los estudiantes y la cantidad de horas
            que los estudiantes leen por entretenimiento, un
            diccionario para la referencia de las filas y otro
            para la referencia de las columnas. 

    """

    print(logic.crear_matriz(datos))

def ejecutar_numero_estudiantes_estrato(datos:DataFrame):

    """

    Pide al usuario que inserte un estrato entre 1 y 6 y
    y ejecuta la opcion de consultar la cantidad de evaluados
    que pertenecen al estrato dado por el ususario.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        numero: int
            Entero que indica la cantidad requerida.

    """
    
    validez = False
    while validez == False:
        estrato = int(input("Ingrese un estrato. Valor de 1 a 6: "))
        if estrato < 1 or estrato > 6:
            print("El estrato ingresado no es valido.")
        else:
            validez = True
            print(logic.numero_estudiantes_estrato(logic.crear_matriz(datos), estrato))

def ejecutar_numero_estudiantes_lectura(datos:DataFrame):

    """

    Pide al usuario que inserte una cantidad de horas con el
    formato indicado y ejecuta la opcion de consultar la
    cantidad de evaluados que leen la cantidad de horas
    insertadas por el ususario.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        numero: int
            Entero que indica la cantidad requerida.

    """

    validez = False
    while validez == False:
        horas = float(input("0.5 para media hora y 1 para una hora. Ingrese las horas con las que desea consultar: "))
        if horas < 0:
            print("El dato insertado no corresponde a la notacion especificada")
        else:
            validez = True
            print(logic.numero_estudiantes_lectura(logic.crear_matriz(datos), horas))

def ejecutar_estrato_mayor_estudiantes(datos:DataFrame):

    """

    Ejecuta la opcion de consultar el estrato con mayor
    cantidad de evaluados.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        numero: int
            Entero que indica la cantidad requerida.

    """

    print(logic.estrato_mayor_estudiantes(logic.crear_matriz(datos)))

def ejecutar_estrato_lectura_mayor(datos:DataFrame):
    
    """

    Ejecuta la opcion de consultar el estrato y el rango de
    lectura diaria en el que se registró el mayor número de
    estudiantes.

    Entradas:

        datos: DataFrame
            Recibe un DataFrame con los datos del archivo
            ingresado por el usuario.

    Retorno:

        tupla: tuple
            Tupla de dos elementos: estrato  y tiempo de
            lectura que poseen el mayor numero de evaluados.

    """
    
    print(logic.estrato_lectura_mayor(logic.crear_matriz_tupla(datos)))

def mostrar_menu():

    """

        Muestra las opciones que el usuario puede ejecutar.

    """

    print("\nBienvenido al analizar de las pruebas saber 11 del año 2020.\n")
    print("1. Cargar el archivo de datos.")
    print("2. Consultar la distribución de la población objeto respecto a la nacionalidad.")
    print("3. Consultar la distribución de la población objeto respecto al género y estrato.")
    print("4. Consultar cuales fueron los 10 mejores departamentos y su promedio.")
    print("5. Consultar los 5 municipios con puntaje más bajo de un departamento.")
    print("6. Consultar los mejores 10 municipios en alguna de las areas evaludas.")
    print("7. Consultar el desempeño por estrato con respecto al puntaje global.")
    print("8. Consultar la relacion entre los alimentos consumidos por los evaluados y el desempeño de estos en alguna de las areas evaluadas.")
    print("9. Consultar una tupla con la matriz entre datos de estrato y tiempos de lectura, un diccionario de las filas y otro de las columnas.")
    print("10. Consultar el número de evaluados por estrato.")
    print("11. Consultar el numero de evaluados que leen diariamente determinadas horas.")
    print("12. Consutlar el estrato con mayor numero de evaluados.")
    print("13. Consultar el estrato y tiempo de lectura con mayor cantidad de evaluados.")
    print("14. Salir de la aplicacion")

def iniciar_aplicacion():

    """
        
        Ejecuta el programa para el usuario.
        
    """

    continuar  = True
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("\nEscriba el indice de la opcion que desea ejecutar: "))
        if opcion_seleccionada == 1:
            datos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_distribucion_nacionalidad(datos)
        elif opcion_seleccionada == 3:
            ejecutar_distribucion_genero_estrato(datos)
        elif opcion_seleccionada == 4:
            ejecutar_desempeño_departamentos(datos)
        elif opcion_seleccionada == 5:
            ejecutar_municipio_puntajes_bajo(datos)
        elif opcion_seleccionada == 6:
            ejecutar_desempeño_municipio_categoria(datos)
        elif opcion_seleccionada == 7:
            ejecutar_desempeño_estratos(datos)
        elif opcion_seleccionada == 8:
            ejecutar_relacion_nutricion_desempenio(datos)
        elif opcion_seleccionada == 9:
            ejecutar_crear_matriz(datos)
        elif opcion_seleccionada == 10:
            ejecutar_numero_estudiantes_estrato(datos)
        elif opcion_seleccionada == 11:
            ejecutar_numero_estudiantes_lectura(datos)
        elif opcion_seleccionada == 12:
            ejecutar_estrato_mayor_estudiantes(datos)
        elif opcion_seleccionada == 13:
            ejecutar_estrato_lectura_mayor(datos)
        elif opcion_seleccionada == 14:
            continuar = False
        else:
            print("Por favor ingrese una opcion válida")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()