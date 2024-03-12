from collections import defaultdict
import re

# Función para leer el archivo línea por línea y detectar patrones repetidos
def detectar_patrones(archivo_entrada):
    patrones = defaultdict(int)
    instrucciones = []

    with open(archivo_entrada, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                patrones[linea] += 1
                instrucciones.append(linea)
    
    # Crear tokens con las líneas repetidas al menos dos veces
    tokens = {}
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    token_count = 0
    for linea, repeticiones in patrones.items():
        if repeticiones >= 2:
            token_id = letras[token_count]
            tokens[token_id] = linea
            token_count += 1

    return instrucciones, tokens

# Función para reemplazar los tokens en el código
def reemplazar_tokens(instrucciones, tokens):
    codigo_final = []
    for instruccion in instrucciones:
        for token_id, patron in tokens.items():
            instruccion = re.sub(patron, token_id, instruccion)
        codigo_final.append(instruccion)
    return codigo_final

# Función para escribir las instrucciones y los tokens en el archivo de salida
def escribir_archivo_salida(instrucciones, tokens, archivo_salida):
    with open(archivo_salida, 'w') as archivo:
        archivo.write("Código con tokens:\n")
        for instruccion in instrucciones:
            archivo.write(instruccion + "\n")
        archivo.write("\nTabla de traducción:\n")
        for token_id, patron in tokens.items():
            archivo.write(f"{token_id}: {patron}\n")

# Nombre de archivo de entrada y salida
archivo_entrada = "Compiler/nuevo_archivo_binario.txt"
archivo_salida = "Compiler/Code_tokens.txt"

# Detectar patrones y reemplazar tokens en el código
instrucciones, tokens = detectar_patrones(archivo_entrada)
codigo_final = reemplazar_tokens(instrucciones, tokens)

# Escribir en el archivo de salida
escribir_archivo_salida(codigo_final, tokens, archivo_salida)

print("Se ha generado el archivo de salida con éxito.")
