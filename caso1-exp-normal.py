import time
import sys
import psutil
import random
import numpy as np

#busqueda binaria
def busqueda_binaria(arreglo, objetivo, izquierda=0, derecha=None):
    if derecha is None: derecha = len(arreglo) - 1
    if izquierda > derecha: return -1 # no se encuentra en el arreglo
    medio = (izquierda + derecha) // 2
    if arreglo[medio] == objetivo: return medio
    elif arreglo[medio] < objetivo : return busqueda_binaria(arreglo, objetivo, medio+1, derecha)
    else : return busqueda_binaria(arreglo, objetivo, izquierda, medio-1)

#estadisticas
def medir_rendimiento(arreglo, objetivo):
    # Medir tiempo
    tiempo_inicio = time.perf_counter()
    resultado = busqueda_binaria(arreglo, objetivo, izquierda=0, derecha=None)
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
        "resultado": resultado,
        "tiempo_ejecucion": tiempo_ejecucion,
        "uso_memoria": uso_memoria,
        "uso_ram": uso_ram,
        "cpu_percent": cpu_percent
    }

def generate_normal_array(size, mean, std_dev):
    arr = np.random.normal(mean, std_dev, size)
    rounded_arr = np.round(arr, decimals=5).tolist()
    return sorted(rounded_arr)

# Parametros de busquedas
size = 1000000
objetivo = np.random.normal(50, 10, 1)
objetivo = np.round(objetivo, decimals=5)
print("--------------------")
print("tamaño arreglo: ",size )
print("numero a buscar: ", objetivo)
print("--------------------")
arreglo = generate_normal_array(size, 50, 10)
#print(arreglo)
metricas = medir_rendimiento(arreglo, objetivo)

print(f"Resultado [indice del arreglo]: {metricas['resultado']}")
print(f"Tiempo de ejecución: {metricas['tiempo_ejecucion']:.6f} segundos")
print(f"Uso de memoria: {metricas['uso_memoria']} bytes")
print(f"Uso de RAM: {metricas['uso_ram']:.2f} MB")
print(f"porcentaje CPU: {metricas['cpu_percent']}%")