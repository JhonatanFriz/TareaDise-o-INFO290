import numpy as np
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

# Distribución normal
def generate_normal_array(size, mean, std_dev):
    arr = np.random.normal(mean, std_dev, size)
    rounded_arr = np.round(arr, decimals=0).tolist()
    return sorted(rounded_arr)

#sample
def sample(array, m, b):
    aux = []
    aux.append(array[0])
    for i in range(b, len(array), b):
        aux.append(array[i])
    return aux

# Tamaño de los arreglos
largo = input("Tamaño arreglos: ")
array_size = int(largo)

# parametros para B y M
m = input("ingrese un m :   ")
m = int(m)
while m > array_size: 
    m = input("ingrese un m :   ")
    m = int(m)
b = input("ingrese un b :   ")
b = int(b)

# Generar los arreglos
# Lineal
linear_array = generate_linear_array(array_size, 10)
print("----- Arreglo LINEAL ----- \n", linear_array)

sample_array_lineal = sample(linear_array, m , b)
print("\n----- Sample LINEAL -----\n",sample_array_lineal)

gap_lineal = gap_coding(linear_array)
print("\n----- Cod-Gaping LINEAL ----- \n", gap_lineal)

print("\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# Normal
normal_array = generate_normal_array(array_size, 50, 10)
print("\n----- Arreglo NORMAL ----- \n", normal_array)

sample_array_normal = sample(normal_array, m, b)
print("\n----- Sample NORNAL ----- \n", sample_array_normal)

gap_normal = gap_coding(normal_array)
print("\n----- Cod-Gaping NORNAL ----- \n", gap_normal)


