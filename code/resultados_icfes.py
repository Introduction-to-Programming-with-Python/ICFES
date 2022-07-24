from numpy import mat
import pandas as pd
import matplotlib.pyplot as plt
from operator import itemgetter
from pandas.core.frame import DataFrame

# PARTE 1.----------------------------------------------------------------------------

# Requerimiento 0.
def cargar_datos(nombre_archivo:str)->DataFrame:

    """
    
    Parameters
    ----------
    nombre_archivo : str
        Nombre del archivo sin extension, que contiene la
        informacion de la prueba ICFES Saber 11.

    Returns
    -------
    DataFrame
        Informacion del archivo CSV leida como DataFrame.

    """

    archivo = pd.read_csv(nombre_archivo)

    return archivo

# PARTE 2.----------------------------------------------------------------------------

# Requerimiento 1.
def distribucion_nacionalidad(datos:DataFrame):

    """

    Calcula la distribucion de nacionalidad entre la poblacion
    evaluada.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    Returns
    -------
        Grafica con la informacion calculada.

    """
    
    datas = datos.iloc[:, 1][datos.NACIONALIDAD != "COLOMBIA"][datos.NACIONALIDAD != "VENEZUELA"].value_counts()
    totales = datos.iloc[:, 1][datos.NACIONALIDAD != "COLOMBIA"][datos.NACIONALIDAD != "VENEZUELA"].count()

    paises = list(datas.index)
    datos = list(datas.values/totales)
 
    dic = {"nacionalidad": paises, "Frecuencia": datos}
    df = pd.DataFrame(dic).set_index("nacionalidad").sort_values(by="nacionalidad").plot(kind='bar', figsize=(15,20), ylabel = "Freuencia", xlabel = "Nacionalidad")
    plt.show()

# Requirimiento 2.
def distribucion_genero_estrato(datos:DataFrame, estrato:str):

    """

   Calcula los procentajes de genero de un estrato.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.
    
    estrato: str
        Estrato del cual se quiere saber la informacion.

    Returns
    -------
        Grafica con la informacion calculada.

    """

    cant_total = (datos.iloc[:, 6][datos.ESTRATO == estrato].value_counts())[0]
    cant_m = (datos.iloc[:, 6][datos.ESTRATO == estrato][datos.GENERO == "M"].value_counts())[0]
    cant_f = (datos.iloc[:, 6][datos.ESTRATO == estrato][datos.GENERO == "F"].value_counts())[0]
    
    porcentaje_m = (cant_m*100)/cant_total
    porcentaje_f = (cant_f*100)/cant_total

    labels = 'F', 'M'
    sizes = [porcentaje_f, porcentaje_m]
    ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=360)
    ax1.axis('equal')
    plt.title(f"Diagrama de tortas para el genero en el estrato {estrato[-1]}")
    plt.ylabel("Estudiantes")
    plt.show()

# PARTE 3.----------------------------------------------------------------------------

# Requerimiento 3.
def desempeño_departamentos(datos:DataFrame):

    """

    Calcula los 10 mejores departamentos tomando como criterio
    el puntaje global.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    Returns
    -------
        Grafica con la informacion calculada.

    """

    departamentos = list((datos.iloc[:, 4].unique()))
    departamentos.sort()

    top = {}

    for i in departamentos:
        promedio = datos.iloc[:, -1][datos.DEPARTAMENTO == i].mean()
        top[i] = promedio

    top = dict(sorted(top.items(), key=itemgetter(1), reverse=True))

    departamentos = list(top.keys())
    departamentos.reverse()
    puntajes = list(top.values())
    puntajes.reverse()

    plt.barh(departamentos[-10:], puntajes[-10:])
    plt.title("Top 10 Departamentos con mejor promedio")
    plt.xlabel("Puntaje global promedio")
    plt.ylabel("Departamento")
    plt.show()

# Requerimiento 4.
def municipio_puntajes_bajo(datos:DataFrame, departamento:str):

    """

    Calcula los municipios con puntajes mas bajos en un
    departamento tomando como criterio el puntaje global.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    departamento: str
        Departamento del cul se quiere saber la informacion.

    Returns
    -------
        Grafica con la informacion calculada.

    """

    datos = datos.loc[:, ["MUNICIPIO", "PUNT_LECTURA_CRITICA", "PUNT_MATEMATICAS", "PUNT_NATURALES", "PUNT_SOCIALES", "PUNT_INGLES", "PUNT_GLOBAL"]][datos.DEPARTAMENTO == departamento]
    municipios = list(datos["MUNICIPIO"].unique())
    municipios.sort()
    
    punt_globales = {}
    for i in municipios:
        promedio = datos.loc[:, "PUNT_GLOBAL"][datos.MUNICIPIO == i].mean()
        punt_globales[i] = promedio
    punt_globales = dict(sorted(punt_globales.items(), key=itemgetter(1)))
    list_municipios = list(punt_globales.keys())[0:5]
    list_municipios.reverse()

    areas = list(datos.columns)[1:-1]

    dic = {}

    for i in areas:
        dic[i] = {}

    for i in dic:
        area = dic[i]
        for l in list_municipios:
            area[l] = 1

    for i in list_municipios:
        for l in areas:
            promedio = round(datos.loc[:, l][datos.MUNICIPIO == i].mean())
            dic[l][i] = promedio

    #df = pd.DataFrame(dic).plot(kind = "barh")
    #plt.show()

    return dic

# Requerimiento 5.
def desempeño_municipio_categoria(datos:DataFrame, categoria:str, materia:str):

    """

    Calcula los 10 mejores municipios en una las areas 
    evaluadas por la prueba ICFES Saber 11.
    
    Parameters
    ----------
    
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    categoria: str
        Area evaluada por la prueba ICFES Saber 11.

    Returns
    -------
        Grafica con la informacion calculada.

    """

    municipios = list((datos.iloc[:, 5].unique()))
    municipios.sort()

    top = {}

    for i in municipios:
        promedio = datos.iloc[:, categoria][datos.MUNICIPIO == i].mean()
        top[i] = promedio

    top = dict(sorted(top.items(), key=itemgetter(1), reverse=True))

    municipios = list(top.keys())
    puntajes = list(top.values())

    plt.barh(municipios[0:10], puntajes[0:10])
    plt.title(f"Desempeño municipal en {materia}")
    plt.xlabel("Puntaje")
    plt.ylabel("Municipio")
    plt.show()

# Requerimiento 6.
def desempenio_estratos(datos:DataFrame):

    """

    Calcula el desempeño de cada estrato.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    Returns
    -------
        Grafica con la informacion calculada.

    """

    datos = datos.loc[:, ["ESTRATO", "PUNT_GLOBAL"]].boxplot(by="ESTRATO", rot=90,figsize=(15,10))  
    plt.title("")
    plt.xlabel("Estrato")
    plt.ylabel("Puntaje global")
    plt.show()

# Requerimiento 7.
def relacion_nutricion_desempenio(datos:DataFrame, grupo_alimenticio:str, categoria:str):
    
    """

    Calcula la relacion entre un grupo alimenticio y el
    desempeño en alguna de las areas.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    grupo_alimenticio: str
        Grupo alimenticio el cual se quiere relacionar.

    caregoria: str
        Area de evaluacion de la prueba la cual se quiere
        relacionar.

    Returns
    -------
        Grafica con la informacion calculada.

    """
    
    datos = datos.loc[:, [grupo_alimenticio, categoria]].boxplot(by=grupo_alimenticio, rot=90,figsize=(15,10))  
    plt.title("")
    plt.xlabel("Alimentacion")
    plt.ylabel(categoria)
    plt.show()

# PARTE 4.----------------------------------------------------------------------------

# Requerimiento 8
def crear_matriz(datos:DataFrame) -> tuple:

    """

    Calcula una tupla de 3 elementos los cuales son:  matriz
    que cruza los estratos de los estudiantes y la cantidad de
    horas que los estudiantes leen por entretenimiento, un
    diccionario para la referencia de las filas y otro para la
    referencia de las columnas. 
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    Returns
    -------
        Tupla con la informacion calculada.

    """

    estratos = datos["ESTRATO"].unique()
    estratos.sort()
    estratos_dict = dict(list(enumerate(estratos)))

    lectura = datos["LECTURA_DIARIA"].unique()
    lectura.sort()
    aux = lectura[2]
    lectura[2] = lectura[1]
    lectura[1] = aux
    lectura_diiict = dict(list(enumerate(lectura)))

    matriz = []

    for estrato in estratos:
        fila = []
        for tiempo in lectura:
            cantidad = datos.iloc[:, 1][datos.ESTRATO == estrato][datos.LECTURA_DIARIA == tiempo].count()
            fila.append(cantidad)
        matriz.append(fila)

    return matriz

def crear_matriz_tupla(datos: DataFrame) -> tuple:


    estratos = datos["ESTRATO"].unique()
    estratos.sort()
    estratos_dict = dict(list(enumerate(estratos)))

    lectura = datos["LECTURA_DIARIA"].unique()
    lectura.sort()
    aux = lectura[2]
    lectura[2] = lectura[1]
    lectura[1] = aux
    lectura_diiict = dict(list(enumerate(lectura)))

    matriz = []

    for estrato in estratos:
        fila = []
        for tiempo in lectura:
            cantidad = datos.iloc[:, 1][datos.ESTRATO == estrato][datos.LECTURA_DIARIA == tiempo].count()
            fila.append(cantidad)
        matriz.append(fila)

    return (matriz, estratos_dict, lectura_diiict)

# Requerimiento 9
def numero_estudiantes_estrato(matriz:list, estrato:int)->int:

    """

    Calcula el numero de estudiantes de un estrato.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    Returns
    -------
        estrato: int
            Estrato del cual se quiere calcular la informacion.

    """

    estrato_lista = []

    if estrato == 1:
        estrato_lista = matriz[0]
    if estrato == 2:
        estrato_lista = matriz[1]
    if estrato == 3:
        estrato_lista = matriz[2]
    if estrato == 4:
        estrato_lista = matriz[3]
    if estrato == 5:
        estrato_lista = matriz[4]
    if estrato == 6:
        estrato_lista = matriz[5]

    numero = 0

    for i in estrato_lista:
        numero += int(i)

    return numero

# Requerimiento 10
def numero_estudiantes_lectura(matriz:list, horas:float)->int:

    """

    Calcula el numero de estudiantes que leen x horas.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    Returns
    -------
        horas: float
            Numero de la cantidad de horas con la cual se
            quiere realizar los calculos.

    """

    columna = []

    if horas == 0:
        columna = [4]

    if horas <= 0.5:
        columna = [0, 1]

    if horas >= 0.5 and horas <= 1:
        columna = [0, 1]

    if horas >= 1 and horas <= 2:
        columna = [1, 2]

    if horas > 2:
        columna = [3]

    numero = 0

    for l in matriz:
        for i in columna:
            numero += l[i]

    return f"\n{numero}\n"

# Requerimiento 11
def estrato_mayor_estudiantes(matriz:list)->str:

    """

    Calcula el estrato con mayor cantidad de estudiantes.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    Returns
    -------
        Estrato calculado.

    """

    dic = {}

    estrato = 1
    suma = 0

    for i in matriz:
        for l in i:
            suma += l
        dic[estrato] = suma
        suma = 0
        estrato += 1

    dic = dict(sorted(dic.items(), key=itemgetter(1), reverse=True))

    for i in dic.keys():
        i = i
        break

    return f"\nEl estrato con mayor numero de evaluados es el {i}.\n"

# Requerimiento 12
def estrato_lectura_mayor(tupla:tuple)->tuple:

    """

    Calcula el estrato y la frecuencia de lectura que posee
    mayor cantidad de estudiantes.
    
    Parameters
    ----------
    datos : DataFrame
        Informacion del archivo CSV leida como DataFrame.

    Returns
    -------
        tuple:
            Tupla con la informacion calculada.

    """

    maximo = 0
    matriz = tupla[0]
    filasss = tupla[1]
    columnas = tupla[2]

    for i in matriz:
        for l in i:
            if l > maximo:
                maximo = l
    
    pos_estrato = 0
    pos_lectura = 0

    for i in range(len(matriz)):
        fila = matriz[i]
        for t in range(len(matriz[0])):
            lectura = fila[t]
            if lectura == maximo:
                pos_estrato = i
                pos_lectura = t

    pos_estrato = filasss[pos_estrato]
    pos_lectura = columnas[pos_lectura]

    return (pos_estrato, pos_lectura)