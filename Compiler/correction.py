def leer_y_transformar(archivo_salida, archivo_codigo, archivo_tabla):
    codigo_con_tokens = []
    tabla_traduccion = {}
    leyendo_codigo = None
    
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
    
    # Escribir la tabla de traducción en un archivo separado
    with open(archivo_tabla, 'w') as file:
        for token, instruccion in tabla_traduccion.items():
            file.write(f"{token}: {instruccion}\n")
    
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
    
    # Escribir el código final en un archivo separado
    with open(archivo_codigo, 'w') as file:
        for instruccion in codigo_final:
            file.write(instruccion + "\n")

# Nombre de archivo de salida
archivo_salida = "Compiler/Code_tokens.txt"
archivo_codigo = "Compiler/codigo_final.txt"
archivo_tabla = "Compiler/tabla_traduccion.txt"

# Leer el archivo de salida y realizar transformaciones
leer_y_transformar(archivo_salida, archivo_codigo, archivo_tabla)

print("Se han actualizado los archivos con el código final y la tabla de traducción.")
