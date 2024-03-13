from collections import defaultdict
import re

# Function to read the file line by line and detect repeated patterns
def detect_patterns(input_file):
    patrones = defaultdict(int)
    instructions = []

    with open(input_file, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                patrones[linea] += 1
                instructions.append(linea)
    
    # Create tokens with lines repeated at least twice
    tokens = {}
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    token_count = 0
    for linea, repeticiones in patrones.items():
        if repeticiones >= 2:
            token_id = letras[token_count]
            tokens[token_id] = linea
            token_count += 1

    return instructions, tokens

# Function to replace tokens in code
def replace_tokens(instructions, tokens):
    final_code = []
    for instruccion in instructions:
        for token_id, patron in tokens.items():
            instruccion = re.sub(patron, token_id, instruccion)
        final_code.append(instruccion)
    return final_code

# Function to write the instructions and tokens to the output file
def write_output_file(instructions, tokens, output_file):
    with open(output_file, 'w') as archivo:
        archivo.write("Código con tokens:\n")
        for instruccion in instructions:
            archivo.write(instruccion + "\n")
        archivo.write("\nTabla de traducción:\n")
        for token_id, patron in tokens.items():
            archivo.write(f"{token_id}: {patron}\n")

# Input and output file name
input_file = "Compiler/new_binary_file.txt"
output_file = "Compiler/Code_tokens.txt"

# Detect patterns and replace tokens in code
instructions, tokens = detect_patterns(input_file)
final_code = replace_tokens(instructions, tokens)

# Write to output file
write_output_file(final_code, tokens, output_file)

print("The output file has been generated successfully.")
