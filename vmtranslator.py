import sys
import os

shorts = {
    "local": "LCL",
    "stack": "SP",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT",
    "static": "16",
    "pointer": "THIS"
}


def nthWord(line, n):
    return line.split(" ")[n]


def push(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        if(nthWord(line, 1) == "constant"):
            asmFile.write("@" + nthWord(line, 2) + "\n")
            asmFile.write("D=A\n")
        else:
            asmFile.write("@" + nthWord(line, 2) + "\n")
            asmFile.write("D=A\n")
            asmFile.write("@" + shorts[nthWord(line, 1)] + "\n")
            asmFile.write("A=M+D\n")
            asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("A=M\n")
        asmFile.write("M=D\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M+1\n")
    return None


def pop(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("@" + shorts[nthWord(line, 1)] + "\n")
        asmFile.write("A=A+" + nthWord(line, 2) + "\n")
        asmFile.write("M=D\n")
    return None


def gt(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=D-M\n")
        asmFile.write("@GREATER{}\n".format(str(num)))
        asmFile.write("D;JGT\n")
        asmFile.write("@LESS{}\n".format(str(num)))
        asmFile.write("0;JMP\n")
        asmFile.write("(GREATER{})\n".format(str(num)))
        asmFile.write("\tM=-1\n")
        asmFile.write("\t@END{}\n".format(str(num)))
        asmFile.write("\t0;JMP\n")
        asmFile.write("(LESS{})\n".format(str(num)))
        asmFile.write("\tM=0\n")
        asmFile.write("(END{})\n".format(str(num)))
    return None


def lt(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=D-M\n")
        asmFile.write("@LESS{}\n".format(str(num)))
        asmFile.write("D;JLT\n")
        asmFile.write("@GREATER{}\n".format(str(num)))
        asmFile.write("0;JMP\n")
        asmFile.write("(LESS{})\n".format(str(num)))
        asmFile.write("\tM=-1\n")
        asmFile.write("\t@END{}\n".format(str(num)))
        asmFile.write("\t0;JMP\n")
        asmFile.write("(GREATER{})\n".format(str(num)))
        asmFile.write("\tM=0\n")
        asmFile.write("(END{})\n".format(str(num)))
    return None


def eq(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=D-M\n")
        asmFile.write("@EQUAL{}\n".format(str(num)))
        asmFile.write("D;JGT\n")
        asmFile.write("@NOTEQUAL{}\n".format(str(num)))
        asmFile.write("0;JMP\n")
        asmFile.write("(EQUAL{})\n".format(str(num)))
        asmFile.write("\tM=-1\n")
        asmFile.write("\t@END{}\n".format(str(num)))
        asmFile.write("\t0;JMP\n")
        asmFile.write("(NOTEQUAL{})\n".format(str(num)))
        asmFile.write("\tM=0\n")
        asmFile.write("(END{})\n".format(str(num)))
    return None


def add(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("A=M-1\n")
        asmFile.write("M=M+D\n")
    return None


def sub(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("A=M-1\n")
        asmFile.write("M=M-D\n")
    return None


def neg(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("M=-M\n")
    return None


def not_(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("M=M&0\n")
    return None


def and_(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("A=M-1\n")
        asmFile.write("M=M&D\n")
    return None


def or_(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("A=M-1\n")
        asmFile.write("M=M|D\n")
    return None


def label(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        label_name = nthWord(line, 1)
        asmFile.write("({}${})\n".format(currFunc, label_name))
        return None


def goto(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        label_name = nthWord(line, 1)
        asmFile.write("@{}${}\n".format(currFunc, label_name))
        asmFile.write("0;JMP\n")
    return None


def if_goto(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        label_name = nthWord(line, 1)
        asmFile.write("@SP\n")
        asmFile.write("A=M-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@{}${}\n".format(currFunc, label_name))
        asmFile.write("D;JEQ\n")
    return None


def function(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        nVars = int(nthWord(line, 2))
        name = nthWord(line, 1)
        asmFile.write("({})\n".format(name))
        for i in range(nVars):
            asmFile.write("@SP\n")
            asmFile.write("A=M\n")
            asmFile.write("M=0\n")
            asmFile.write("@SP\n")
            asmFile.write("M=M+1\n")
    return name

def call(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        retAddr = str(num + 1)
        nArgs = str(nthWord(line, 2))
        # Push return address
        asmFile.write("@{}\n".format(retAddr))
        asmFile.write("D=A\n")
        asmFile.write("@SP\n")
        asmFile.write("A=M\n")
        asmFile.write("M=D\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M+1\n")
        # Push LCL, ARG, THIS, THAT
        push_things = ["LCL", "ARG", "THIS", "THAT"]
        for thing in push_things:
            asmFile.write("@{}\n".format(thing))
            asmFile.write("D=M\n")
            asmFile.write("@SP\n")
            asmFile.write("A=M\n")
            asmFile.write("M=D\n")
            asmFile.write("@SP\n")
            asmFile.write("M=M+1\n")
        # ARG = SP - nArgs - 5
        asmFile.write("@SP\n")
        asmFile.write("D=M\n")
        asmFile.write("@{}\n".format(nArgs))
        asmFile.write("D=D-A\n")
        asmFile.write("@5\n")
        asmFile.write("D=D-A\n")
        # LCL = SP
        asmFile.write("@SP\n")
        asmFile.write("D=M\n")
        asmFile.write("@LCL\n")
        asmFile.write("M=D\n")
        # goto g
        asmFile.write("@{}\n".format(nthWord(line, 1)))
        asmFile.write("0;JMP\n")
    return None

def return_(currFunc, vmFile, line, file, num):
    with open(file, "a") as asmFile:
        # frame = LCL
        asmFile.write("@LCL\n")
        asmFile.write("D=M\n")
        asmFile.write("@frame\n")
        asmFile.write("M=D\n")
        asmFile.write("@5\n")
        asmFile.write("D=A\n")
        asmFile.write("@frame\n")
        asmFile.write("A=A-D\n")
        asmFile.write("D=M\n")
        asmFile.write("@retAddr\n")
        asmFile.write("M=D\n")
        # *ARG = pop
        asmFile.write("@SP\n")
        asmFile.write("A=A-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@SP\n")
        asmFile.write("M=M-1\n")
        asmFile.write("@ARG\n")
        asmFile.write("M=D\n")
        # SP = ARG + 1
        asmFile.write("D=M+1\n")
        asmFile.write("@SP\n")
        asmFile.write("M=D\n")
        # THAT = *(frame - 1)
        asmFile.write("@frame\n")
        asmFile.write("A=A-1\n")
        asmFile.write("D=M\n")
        asmFile.write("@THAT\n")
        asmFile.write("M=D\n")
        # THIS = *(frame - 2)
        asmFile.write("@2\n")
        asmFile.write("D=A\n")
        asmFile.write("@frame\n")
        asmFile.write("A=A-D\n")
        asmFile.write("D=M\n")
        asmFile.write("@THIS\n")
        asmFile.write("M=D\n")
        # ARG = *(frame - 3)
        asmFile.write("@3\n")
        asmFile.write("D=A\n")
        asmFile.write("@frame\n")
        asmFile.write("A=A-D\n")
        asmFile.write("D=M\n")
        asmFile.write("@ARG\n")
        asmFile.write("M=D\n")
        # LCL = *(frame - 4)
        asmFile.write("@4\n")
        asmFile.write("D=A\n")
        asmFile.write("@frame\n")
        asmFile.write("A=A-D\n")
        asmFile.write("D=M\n")
        asmFile.write("@LCL\n")
        asmFile.write("M=D\n")
        # goto retAddr
        asmFile.write("@retAddr\n")
        asmFile.write("0;JMP\n")
    return None


cmds = {
    "push": push,
    "pop": pop,
    "gt": gt,
    "lt": lt,
    "eq": eq,
    "add": add,
    "sub": sub,
    "neg": neg,
    "not": not_,
    "and": and_,
    "or": or_,
    "label": label,
    "function": function,
    "call": call,
    "return": return_,
    "goto": goto,
    "if-goto": if_goto
}

vmDir = sys.argv[1]
output = sys.argv[2]
for vmFileName in os.listdir(vmDir):
    print(vmDir + "/" + vmFileName)
    with open(vmDir + "/" + vmFileName, "r", encoding="utf-8") as vmFile:
        lines = vmFile.readlines()
        currFunc = ""
        for i in range(len(lines)):
            line = lines[i]
            line = line.replace("\n", "")
            retVal = cmds[nthWord(line, 0)](currFunc, vmFileName, line, output, i)
            if retVal is not None:
                if retVal is not "returned":
                    currFunc = retVal
                else:
                    currFunc = ""

with open(sys.argv[2], "a") as asmFile:
    # set SP to 256
    asmFile.write("@256\n")
    asmFile.write("D=A\n")
    asmFile.write("@SP\n")
    asmFile.write("M=D\n")
    # set LCL, ARG, THIS, THAT to -1
    things = ["LCL", "THIS", "THAT", "ARG"]
    for thing in things:
        asmFile.write("@{}\n".format(thing))
        asmFile.write("M=-1\n")
    asmFile.write("@Sys.init\n")
    asmFile.write("0;JMP\n")
    asmFile.write("(END)\n")
    asmFile.write("@END\n")
    asmFile.write("@0;JMP\n")
