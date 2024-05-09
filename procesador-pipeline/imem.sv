module imem (input logic [31:0] pc,
				output logic [31:0] instruction);
	
	logic [31:0] imem_ROM[399:0];
	
	initial
	
		//Lee de memoria las intrucciones
		$readmemh("/home/guillen/Documents/TEC/Proyecto diseño/Proyecto_de_Dise-o_Compresor_y_Descompresor_de_codigo_ensamblador-1/procesador-pipeline/instructions.txt", imem_ROM);
		
		
	assign instruction = imem_ROM[pc[31:0]];
	
endmodule 