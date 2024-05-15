module imem (input logic [31:0] pc,
				output logic [31:0] instruction);
	
	logic [31:0] imem_ROM[399:0];
	
	initial
	
		//Lee de memoria las intrucciones
		$readmemh("/home/guillen/Documents/VectorArchitecture-Develop/procesador-pipeline/instructions.txt", imem_ROM);
		
		
	assign instruction = imem_ROM[pc[31:0]];
	
endmodule 