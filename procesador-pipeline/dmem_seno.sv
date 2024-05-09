module dmem_seno (input logic [31:0] address,
				output logic [31:0] rd);
	
	logic signed [31:0] dmem_seno[0:8099];
	
	initial
	
		//Lee valores del seno
		$readmemh("/home/guillen/Documents/TEC/Proyecto diseño/Proyecto_de_Dise-o_Compresor_y_Descompresor_de_codigo_ensamblador-1/procesador-pipeline/seno.txt", dmem_seno);
		
		
	assign rd = dmem_seno[address[31:0]];
	
endmodule 