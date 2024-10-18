import random
# PARA MOSTRAR MATRICES
def mostrar_matriz(matriz):
    
    for fila in matriz: 
        
        for elemento in fila:
         print(elemento,end=" ")
        
        print()
# -------------------------------

def ordenar_matriz(lista):
    
    tamanio_lista = len(lista)
    
    for i in range(0,tamanio_lista - 1): # 3 
        
        for j in range(0, tamanio_lista - 1):
            
            if lista[j] > lista[j+1]:
                
                aux = lista[j]
                
                lista[j] = lista [j+1]
                
                lista[j+1] = aux
                
    return lista

def convertir_matriz_lista(matriz,filas):
    
    lista = [elemento for fila in matriz for elemento in fila]

    lista_ordenada = ordenar_matriz(lista)

    matriz_ordenada = []

    for i in range(0, len(lista_ordenada), filas):
    
        matriz_ordenada += [(lista_ordenada[i:i + filas])]
        

    return matriz_ordenada
    
def sumatoria_filas(filas_sumadas):
    
    sumatoria = 0

    for fila in filas_sumadas:
        for elemento in fila:
            sumatoria += elemento 

    return sumatoria

def ordenar_sumas(filas_sumadas, filas):
    
    sumas_con_indices = []

    for i in range(filas):
        
        sumas_con_indices += [((filas_sumadas[i], i+1))]

    #Metodo burbuja
    for i in range(0, filas-1):
    
        for j in range(0, filas-1):
            if sumas_con_indices[j][0] < sumas_con_indices[j+1][0]:
            
                aux = sumas_con_indices[j]
            
                sumas_con_indices[j] = sumas_con_indices[j+1]
            
                sumas_con_indices[j+1] = aux

    return sumas_con_indices
    
def sumar_filas(matriz):
    
    filas_sumadas = []

    for fila in matriz:
        
        suma = 0
        
        for elemento in fila:
            
            suma += elemento 
        
        filas_sumadas += [[suma]] # Guardar la suma en la nueva matriz como una lista
    
    return filas_sumadas
               
def llenar_matriz(filas,columnas,opcion):
    
    print()
    print("La matriz se llena de izquierda a derecha,\nsiendo la pocision 1.1 (fila 1, columna 1)\ndonde se ubica el primer valor, la posicion\n1.2 el segundo valor, y asi sucesivamente.")
    print()
    
    matriz = []
    
    for i in range(filas):
        
        fila = []
        
        for j in range(columnas):
            
            # MANUAL
            if opcion == 1:
                
                valor = int(input(f"Ingrese el valor de la posicion {i+1}.{j+1} "))
                
                while valor < 1 or valor > 999:
                    valor = int(input("Ingrese valores entre 1 y 999: "))
                
                fila += [valor]
                
            # ALEATORIO
            if opcion == 2:
                
                fila += [random.randint(1,999)]
                
        matriz += [(fila)]

    return matriz

#-------------------------------------------------------------------
def main():
    """
    1. Cargar una Lista de números decimales de tamaño MXN y mostrar los datos
    cargados. El tamaño de la Lista debe ser solicitado e ingresado por el usuario,
    indicando un valor entero para las filas y un valor entero para las columnas, el
    valor mínimo valido debe ser de 3x2, crear la Lista y solicitar los valores
    numéricos para cargar de datos en cada posición. La carga de los datos puede ser
    manual, donde los datos serán ingresados por el usuario o aleatoria, donde los
    números serán generados automáticamente, ambos casos en el rango de 1 a 999.
    El sistema preguntara al usuario como quiere hacer la carga de valores. (2.5 ptos)
    """
    filas = int(input("Ingrese el numero de filas de la matriz: "))
    columnas = int(input("Ingrese el numero de columnas de la matriz: "))

    while filas < 3 or columnas < 2:
        print("La matriz debe ser mayor o igual a 3 filas y 2 columnas. Intente nuevamente.")
        filas = int(input("Ingrese el numero de filas de la matriz "))
        columnas = int(input("Ingrese el numero de columnas de la matriz "))
    
    opcion = int(input("Ingrese una opcion:\n1: Rellenar matriz de manera MANUAL.\n2: Rellenar matriz de manera ALEATORIA\n"))
    while opcion < 0 or opcion > 2:
        opcion = int(input("Ingrese 1 o 2: "))
    
    matriz = llenar_matriz(filas,columnas,opcion)
    
    """
    2. Mostrar la Lista resultante por pantalla en formato de Lista (filas y columnas). (0.25 ptos)
    """
    print(" \nLa matriz que se creo es:")   
    mostrar_matriz(matriz)
    
    """
    3. Generar una nueva Lista de N filas por 1 columna que contenga en cada celda de
    la columna la sumatoria de las celdas de cada una de las filas de la Lista cargada
    en el punto 1. (2 ptos)
    """
    filas_sumadas = sumar_filas(matriz)
    """
    4. Mostrar la Lista resultante por pantalla. (0.25 ptos)
    """
    print(" \nLa suma de cada fila de la matriz es:")
    mostrar_matriz(filas_sumadas)
    
    """
    5. Generar una nueva Lista de tamaño N filas por 2 columnas donde la primer
    columna contenga los valores calculados en el punto 3 pero ordenados de
    Mayor a Menor, y en la segunda columna asignar el valor de la fila que poseía
    originalmente en la Lista del punto 3. (3.25 ptos)
    """
    sumas_con_indices = ordenar_sumas(filas_sumadas,filas)
    
    """
    6. Mostrar la Lista resultante por pantalla. (0.25 ptos)
    """
    print(" \nSumas ordenadas de mayor a menor\ny las respectivas posiciones donde se encontraban")
    mostrar_matriz(sumas_con_indices)
    
    """
    7. Finalmente sume los elementos de la columna 1 de la Lista del punto 5 y
    muestre el resultado de la sumatoria por pantalla. (1.5 pto)
    """
    sumatoria = sumatoria_filas(filas_sumadas)
    print(" \nLa suma total de los valores anteriores es ",sumatoria)

    # ORDENAR MATRIZ ORIGINAL DE MENOR A MAYOR
    matriz_ordenada = convertir_matriz_lista(matriz,filas)
    print(" \nMatriz ordenada de menor a mayor:")
    mostrar_matriz(matriz_ordenada)

#Ejecutar
main()
