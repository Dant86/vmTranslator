@256
D=A
@SP
M=D
(Main.fibonacci)
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
D=D-M
@LESS3
D;JLT
@GREATER3
0;JMP
(LESS3)
	M=-1
	@END3
	0;JMP
(GREATER3)
	M=0
(END3)
@SP
A=M-1
D=M
@Main.fibonacci$IF_TRUE
D;JEQ
@Main.fibonacci$IF_FALSE
0;JMP
(Main.fibonacci$IF_TRUE)
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@frame
M=D
@5
D=A
@frame
A=A-D
D=M
@retAddr
M=D
@SP
A=A-1
D=M
@SP
M=M-1
@ARG
M=D
D=M+1
@SP
M=D
@frame
A=A-1
D=M
@THAT
M=D
@2
D=A
@frame
A=A-D
D=M
@THIS
M=D
@3
D=A
@frame
A=A-D
D=M
@ARG
M=D
@4
D=A
@frame
A=A-D
D=M
@LCL
M=D
@retAddr
0;JMP
(Main.fibonacci$IF_FALSE)
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
M=M-D
@14
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@1
D=D-A
@5
D=D-A
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
M=M-D
@18
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@1
D=D-A
@5
D=D-A
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
M=M+D
@LCL
D=M
@frame
M=D
@5
D=A
@frame
A=A-D
D=M
@retAddr
M=D
@SP
A=A-1
D=M
@SP
M=M-1
@ARG
M=D
D=M+1
@SP
M=D
@frame
A=A-1
D=M
@THAT
M=D
@2
D=A
@frame
A=A-D
D=M
@THIS
M=D
@3
D=A
@frame
A=A-D
D=M
@ARG
M=D
@4
D=A
@frame
A=A-D
D=M
@LCL
M=D
@retAddr
0;JMP
(Sys.init)
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
@3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@1
D=D-A
@5
D=D-A
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Sys.init$WHILE)
@Sys.init$WHILE
0;JMP
@LCL
M=-1
@THIS
M=-1
@THAT
M=-1
@ARG
M=-1
@Sys.init
0;JMP
(END)
@END
0;JMP