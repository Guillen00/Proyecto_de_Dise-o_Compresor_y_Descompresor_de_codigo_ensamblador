module m_descompresor(input logic [31:0] pc,
                output logic [31:0] instruction);
	 //Inicialice buffers
    logic [31:0] final_code[0:400];
	 logic [35:0] translator_table [0:9];
	 logic [31:0] buffer;
	 logic [3:0] counter_tmp;
	 logic [31:0] instruction_tmp , less_pc;
    //Read documents 
	 initial begin
    $readmemh("/home/guillen/intelFPGA_lite/22.1std/final_code.txt", final_code);
	 $readmemh("/home/guillen/intelFPGA_lite/22.1std/traduction_table.txt", translator_table);
	 end

    // Escribe en memoria 	
    always_ff @(pc)
        begin
			  //count of pc
			  if (pc== 31'h00000000) less_pc =0;
			  //counter_tmp count the pc when it need to be repeat
			  if (counter_tmp == 4'h1) begin
					instruction_tmp = buffer;
					counter_tmp = 4'h0;
			  end
			  else begin
				  //here identify the token because has less value
				  if (final_code[pc-less_pc] < 32'h00000010)begin
						//search tokens in the translation table
						case (final_code[pc-less_pc])
							4'ha: instruction_tmp = translator_table[0][31:0];
							4'hb: instruction_tmp = translator_table[1][31:0];
							4'hc: instruction_tmp = translator_table[2][31:0];
							default: instruction_tmp = translator_table[2][31:0];
						endcase
						//Save the instruction on the buffer
						buffer = instruction_tmp;
						counter_tmp = 4'h1;
						less_pc ++;
				  end
				  else begin
						//Take out the normal instruction
						instruction_tmp = final_code[pc-less_pc];
				  end 
			  
			  end
        end
     assign instruction = instruction_tmp;





endmodule