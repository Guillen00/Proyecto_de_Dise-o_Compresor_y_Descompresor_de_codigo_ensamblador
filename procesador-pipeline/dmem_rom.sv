module dmem_rom (input logic [31:0] address,
				output logic [31:0] rd);
	
	//logic [31:0] dmem_ROM[0:8099];
	logic [31:0] dmem_ROM[0:90000];
	
	initial
	
		//Lee de memoria
		$readmemh("/home/guillen/Documents/TEC/Proyecto diseño/Proyecto_de_Dise-o_Compresor_y_Descompresor_de_codigo_ensamblador-1/procesador-pipeline/imageData.txt", dmem_ROM);
		
		
	assign rd = dmem_ROM[address[31:0]];
	
endmodule 