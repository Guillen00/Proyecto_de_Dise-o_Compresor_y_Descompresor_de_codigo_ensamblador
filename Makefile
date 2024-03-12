py = python3

all:
	$(py) Compilador_Compresor.py

comp:
	$(py) Compiler/compiler.py
	$(py) Compiler/bin_hex.py
	$(py) Compiler/tokens.py
	$(py) Compiler/correction.py

clean:
	rm -f compressed.txt
