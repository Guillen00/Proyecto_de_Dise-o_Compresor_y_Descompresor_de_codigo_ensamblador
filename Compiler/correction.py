# Función para leer el archivo de salida y realizar las transformaciones
def leer_y_transformar(archivo_salida):
    codigo_con_tokens = []
    tabla_traduccion = {}
    with open(archivo_salida, 'r') as archivo:
        for linea in archivo:
            if linea.startswith("Código con tokens:"):
                leyendo_codigo = True
            elif linea.startswith("Tabla de traducción:"):
                leyendo_codigo = False
            elif leyendo_codigo:
                codigo_con_tokens.append(linea.strip())
            else:
                token, instruccion = linea.strip().split(": ")
                tabla_traduccion[token] = instruccion
    
    # Realizar transformaciones en el código
    codigo_final = []
    i = 0
    while i < len(codigo_con_tokens):
        if i+1 < len(codigo_con_tokens) and codigo_con_tokens[i] == codigo_con_tokens[i+1]:
            codigo_final.append(codigo_con_tokens[i])
            i += 1
        else:
            codigo_final.append(tabla_traduccion.get(codigo_con_tokens[i], codigo_con_tokens[i]))
        i += 1
    
    return codigo_final, tabla_traduccion

# Nombre de archivo de salida
archivo_salida = "Compiler/Code_tokens.txt"

# Leer el archivo de salida y realizar transformaciones
codigo_final, tabla_traduccion = leer_y_transformar(archivo_salida)

# Reescribir el archivo original con el código final y la tabla de traducción
with open(archivo_salida, 'w') as archivo:
    archivo.write("Código con tokens:\n")
    for instruccion in codigo_final:
        archivo.write(instruccion + "\n")
    archivo.write("\nTabla de traducción:\n")
    for token, instruccion in tabla_traduccion.items():
        archivo.write(f"{token}: {instruccion}\n")

print("Se ha actualizado el archivo con el código final y la tabla de traducción.")
