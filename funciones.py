"TRABAJO 3: EJECUCIÓN DEL PRESUPUESTO DE INVERSIONES"
"El objetivo de este trabajo es hacer un análisis de las inversiones realizadas" 
"por el Ayuntamiento de Madrid para hacer una comparativa por años y distritos."

"------ FUNCIONES ------"

# LIBRERÍAS
import pandas as pd

# VARIABLES FICHEROS DE DATOS
path = "data/"
extension = ".csv"

# FUNCIÓN 1: Crear una función que reciba un distrito y una lista de años y devuelva 
# un diccionario con el número de inversiones y el total de estas en el distrito esos años.
def inversionesTotalesDistrito (distrito, lista_años) :
    """funcion que recibe un distrito y una lista de años y devuelve un diccionario con las inversiones y el total de estas en esos años"""
    # Variable que contendrá el número total de inversiones en el distrito
    numero_inversiones = 0
    # Variable que contendrá el total invertido en dicho distrito
    total_inversiones = 0
    # Variable que contendrá los datos de cada uno de los años
    datos_años = []
    # Se leen los datos de los ficheros .csv para cada uno de los años
    for año in lista_años :
        # Se añaden a la variable datos_años
        datos_años.append(pd.read_csv(path + año + extension, encoding='latin1', sep=';'))
    # Para cada año...
    for datos in datos_años :
        # Título columnas involucradas en el cálculo
        columna_distrito = "Distrito"
        columna_inversion = "Pagos Real"
        # Para cada fila...
        for i in range(datos.shape[0]) :
            # Si el valor de la columna distrito coincide con el parámetro que recibe la función
            if datos.iloc[i][columna_distrito] == distrito :
                # Se aumenta en 1 el número de inversiones
                numero_inversiones += 1
                # Se suma al total invertido el valor de dicha inversión
                total_inversiones += float(datos.iloc[i][columna_inversion].replace(".","").replace(",",".").replace("\x80",""))
    # Una vez finalizado el cálculo se devuelve un diccionario con los dos valores (el valor en euros se limita a 2 decimales)
    return {("NÚMERO DE INVERSIONES, DISTRITO " + str(distrito)) : numero_inversiones, "TOTAL (€)" : float("{0:.2f}".format(total_inversiones))}

# FUNCIÓN 2: Crear una función que reciba una línea de inversión y una lista de años y devuelva 
# un diccionario con el número de inversiones y el total de estas en la línea de inversión esos años.
def inversionesTotalesLineaInversion (linea_inversion, lista_años) :
    """funcion que recibe una linea de inverson y una lista de años y devuelve un diccionario con el numero de inversiones y el total de estas en esos años"""
    # Variable que contendrá el número total de inversiones en la línea de inversión
    numero_inversiones = 0
    # Variable que contendrá el total invertido en dicha línea de inversión
    total_inversiones = 0
    # Variable que contendrá los datos de cada uno de los años
    datos_años = []
    # Se leen los datos de los ficheros .csv para cada uno de los años
    for año in lista_años :
        # Se añaden a la variable datos_años
        datos_años.append(pd.read_csv(path + año + extension, encoding='latin1', sep=';'))
    # Para cada año...
    for datos in datos_años :
        # Título columnas involucradas en el cálculo
        columna_linea_inversion = "Línea Inversión"
        columna_inversion = "Pagos Real"
        # Para cada fila...
        for i in range(datos.shape[0]) :
            # Si el valor de la columna línea de inversión coincide con el parámetro que recibe la función
            if datos.iloc[i][columna_linea_inversion] == linea_inversion :
                # Se aumenta en 1 el número de inversiones
                numero_inversiones += 1
                # Se suma al total invertido el valor de dicha inversión
                total_inversiones += float(datos.iloc[i][columna_inversion].replace(".","").replace(",",".").replace("\x80",""))
    # Una vez finalizado el cálculo se devuelve un diccionario con los dos valores (el valor en euros se limita a 2 decimales)
    return {("NÚMERO DE INVERSIONES, LÍNEA INVERSIÓN " + str(linea_inversion)) : numero_inversiones, "TOTAL (€)" : float("{0:.2f}".format(total_inversiones))}

# FUNCIÓN OPCIONAL: Crear una función que reciba una lista de años, un distrito y una cantidad n, y devuelva 
# un diccionario con el número de modificaciones presupuestarias superiores a la cantidad n y el total de estas.
def modificacionesPresupuestariasTotalesDistrito (distrito, lista_años, n) :
    # Variable que contendrá el número total de modificaciones presupuestarias superiores a 'n' del distrito
    numero_modificaciones = 0
    # Variable que contendrá el total de las modificaciones presupuestarias superiores a 'n' en dicho distrito
    total_modificaciones = 0
    # Variable que contendrá los datos de cada uno de los años
    datos_años = []
    # Se leen los datos de los ficheros .csv para cada uno de los años
    for año in lista_años :
        # Se añaden a la variable datos_años
        datos_años.append(pd.read_csv(path + año + extension, encoding='latin1', sep=';'))
    # Para cada año...
    for datos in datos_años :
        # Título columnas involucradas en el cálculo
        columna_distrito = "Distrito"
        columna_modificado = "Modifc. "
        # Para cada fila...
        for i in range(datos.shape[0]) :
            # Si el valor de la columna distrito coincide con el parámetro que recibe la función
            if datos.iloc[i][columna_distrito] == distrito :
                # Valor de la modificacion presupuestaria en dicha fila
                valor_modificacion = float(datos.iloc[i][columna_modificado].replace(".","").replace(",",".").replace("\x80",""))
                # Si el valor es superior al parámetro 'n'...
                if valor_modificacion > n :
                    # Se aumenta en 1 el número de modificaciones
                    numero_modificaciones += 1
                    # Se suma al total invertido el valor de dicha modificación
                    total_modificaciones += valor_modificacion
    # Una vez finalizado el cálculo se devuelve un diccionario con los dos valores (el valor en euros se limita a 2 decimales)
    return {("NÚMERO DE MODIFICACIONES PRESUPUESTARIAS > " + str(n) + "€, DISTRITO " + str(distrito)) : numero_modificaciones, "TOTAL (€)" : float("{0:.2f}".format(total_modificaciones))}


"------ TESTS ------"

# FUNCIÓN 1
print(inversionesTotalesDistrito(201, ["2014"]))
print(inversionesTotalesDistrito(201, ["2014", "2015", "2016", "2017", "2018"]))

# FUNCIÓN 2
print(inversionesTotalesLineaInversion(3, ["2014"]))
print(inversionesTotalesLineaInversion(3, ["2014", "2015", "2016", "2017", "2018"]))

# FUNCIÓN OPCIONAL
print(modificacionesPresupuestariasTotalesDistrito(201, ["2014"], 10000.85))
print(modificacionesPresupuestariasTotalesDistrito(201, ["2014", "2015", "2016", "2017", "2018"], 10000.85))
