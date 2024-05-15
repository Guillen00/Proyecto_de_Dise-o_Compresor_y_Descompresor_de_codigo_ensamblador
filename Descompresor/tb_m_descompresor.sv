module tb_m_descompresor;

    // Parámetros del testbench
    localparam CLK_PERIOD = 10; // Período del reloj en unidades de tiempo
    logic clk; // Señal de reloj
    logic [31:0] pc; // Señal de dirección de programa
    logic [31:0] instruction; // Señal de instrucción

    // Instanciar el módulo bajo prueba
    m_descompresor dut (
        .pc(pc),
        .instruction(instruction)
    );

    // Generar el reloj
    always #((CLK_PERIOD / 2)) clk = ~clk;

    // Generar estímulos
    initial begin
        clk = 0; // Inicializar el reloj en bajo
        pc = 32'h00000000; // Dirección de programa para probar
        #20;
        pc = 32'h00000001; // Cambiar la dirección de programa
        #20;
		  pc = 32'h00000002; // Cambiar la dirección de programa
        #20;
		  pc = 32'h00000003; // Cambiar la dirección de programa
        #20;
		  pc = 32'h00000004; // Cambiar la dirección de programa
        #20;
		  pc = 32'h00000005; // Cambiar la dirección de programa
        #20;
		  pc = 32'h00000006; // Cambiar la dirección de programa
        #20;
		  pc = 32'h00000007; // Cambiar la dirección de programa
        #20;
		  pc = 32'h00000008; // Cambiar la dirección de programa
        #20;
        // Añadir más casos de prueba según sea necesario
        $stop; // Detener la simulación al final del testbench
    end

    // Monitorear las señales de salida
    always @(posedge clk) begin
        $display("Instrucción en PC = %h: %h", pc, instruction);
    end

endmodule
