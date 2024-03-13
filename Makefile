py = python3

all:
	$(py) Compiler/compiler.py
	$(py) Compiler/bin_hex.py
	$(py) Compiler/tokens.py
	$(py) Compiler/correction.py

comp:
	$(py) Compiler/compiler.py
	$(py) Compiler/bin_hex.py
	$(py) Compiler/tokens.py
	$(py) Compiler/correction.py

clean:
	rm -f compressed.txt
