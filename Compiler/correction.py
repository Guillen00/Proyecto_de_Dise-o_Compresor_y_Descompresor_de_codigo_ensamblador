# Read and tranform the code with traduction table
def read_and_transform(output_file, code_file, table_file):
    codigo_con_tokens = []
    tabla_traduccion = {}
    leyendo_codigo = None
    
    with open(output_file, 'r') as archivo:
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
    
    # Write the translation table to a separate file
    with open(table_file, 'w') as file:
        for token, instruccion in tabla_traduccion.items():
            file.write(f"{token}: {instruccion}\n")
    
    # Perform transformations in the code
    codigo_final = []
    i = 0
    while i < len(codigo_con_tokens):
        if i+1 < len(codigo_con_tokens) and codigo_con_tokens[i] == codigo_con_tokens[i+1]:
            codigo_final.append(codigo_con_tokens[i])
            i += 1
        else:
            codigo_final.append(tabla_traduccion.get(codigo_con_tokens[i], codigo_con_tokens[i]))
        i += 1
    
    # Write the final code to a separate file
    with open(code_file, 'w') as file:
        for instruccion in codigo_final:
            file.write(instruccion + "\n")

# Output file name
output_file = "Compiler/Code_tokens.txt"
code_file = "Compiler/final_code.txt"
table_file = "Compiler/traduction_table.txt"

# Read the output file and perform transformations
read_and_transform(output_file, code_file, table_file)

print("The files with the final code and the translation table have been updated.")
