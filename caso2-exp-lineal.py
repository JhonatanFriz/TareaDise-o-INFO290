import time
import sys
import psutil
import random

#gap coding
def gap_coding(arreglo):
    if not arreglo:
        return []
    
    gaps = [arreglo[0]]  # El primer elemento se mantiene igual
    
    for i in range(1, len(arreglo)):
        gap = arreglo[i] - arreglo[i-1]
        gaps.append(gap)
    
    return gaps

# Distribución lineal
def generate_linear_array(size, epsilon):
    arr = [random.randint(0, epsilon)]
    for i in range(1, size):
        arr.append(arr[-1] + random.randint(0, epsilon))
    return arr

#sample
def sample(array, m, b):
    aux = []
    aux.append(array[0])
    for i in range(b, len(array), b):
        aux.append(array[i])
        if len(aux) == m:
            break
    return aux

#Busqueda binaria con sample
def busqueda_binaria_sample(sample,objetivo, izquierda=0, derecha=None):
    if derecha is None:             derecha = len(sample)-1
    if izquierda > derecha:         return derecha

    medio = (izquierda+derecha) // 2

    if sample[medio] == objetivo:   return medio
    elif sample[medio] < objetivo:
        return busqueda_binaria_sample(sample, objetivo, medio+1, derecha)
    else:
        return busqueda_binaria_sample(sample, objetivo, izquierda, medio-1)

#gap-coding a arreglo original
#vamos trasformando al original uno por uno ya que
#aumenta el trabajo si transformamos el arreglo entero

def inversa_gc(indice, lineal_gc, lineal_sample, b):
    aux = [lineal_sample[indice] + lineal_gc [indice*b+1]]
    if lineal_sample[indice] == objetivo : 
        return indice
    else :
        for i in range(1,b):
            aux.append(aux[-1]+(lineal_gc[indice*b+i+1]))
            if objetivo == aux[i] : 
                return i
            else : 
                if objetivo < aux[i] :
                    return -1

def medir_rendimiento(arreglo, objetivo):
    # Medir tiempo
    tiempo_inicio = time.perf_counter()
    indice = busqueda_binaria_sample(lineal_sample,objetivo, izquierda=0, derecha=None)
    arr = inversa_gc(indice,lineal_gc,lineal_sample,b) 
    tiempo_fin = time.perf_counter()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio

    # Medir uso de memoria
    uso_memoria = sys.getsizeof(arreglo) + sys.getsizeof(objetivo)

    # Medir uso de RAM
    proceso = psutil.Process()
    uso_ram = proceso.memory_info().rss / 1024 / 1024  # en MB

    # Medir coste computacional (aproximado por el uso de CPU)
    cpu_percent = psutil.cpu_percent()

    return {
        "resultado": arr,
        "tiempo_ejecucion": tiempo_ejecucion,
        "uso_memoria": uso_memoria,
        "uso_ram": uso_ram,
        "cpu_percent": cpu_percent
    }

# parametros del arreglo incial lineal
array_size = 1000000
objetivo = random.randint(1,array_size)
print("--------------------")
print("tamaño arreglo: ",array_size )
print("numero a buscar: ", objetivo)
print("--------------------")

m = 1000
b = round(array_size/m)

#Main
lineal_array = generate_linear_array(array_size, 10)
lineal_sample = sample(lineal_array, m, b)
indice = busqueda_binaria_sample(lineal_sample,objetivo, izquierda=0, derecha=None)
print("Intervalo de buqueda del Sample: ",lineal_sample[indice : indice + 2])
lineal_gc = gap_coding(lineal_array)
metricas = medir_rendimiento(lineal_sample, objetivo)
print(f"Resultado, Indice de Gap-Coding: {metricas['resultado']}")
print(f"Tiempo de ejecución: {metricas['tiempo_ejecucion']:.6f} segundos")
print(f"Uso de memoria: {metricas['uso_memoria']} bytes")
print(f"Uso de RAM: {metricas['uso_ram']:.2f} MB")
print(f"porcentaje CPU: {metricas['cpu_percent']}%")

# parametros para B y M
# m = input("ingrese un m :   ")
# m = int(m)
# while m > array_size: 
#     m = input("ingrese un m :   ")
#     m = int(m)
# b = input("ingrese un b :   ")
# b = int(b)
