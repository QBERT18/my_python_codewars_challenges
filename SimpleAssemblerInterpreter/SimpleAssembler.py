registers = {}


def simple_assembler(program):
    iterator(program, 0)


def iterator(program, programStart):
    for i in range(programStart, len(program)):
        command = program[i].split()
        interprete(program, command, i)


def interprete(program, command, commandIndex):
    if command[0] == "mov":
        mov(command[1], command[2])
    elif command[0] == "inc":
        inc(command[1])
    elif command[0] == "dec":
        dec(command[1])
    elif command[0] == "jnz":
        jnz(command[1], command[2], program, commandIndex)


def mov(register, value):
    if not value.isalpha():
        registers[register] = value
    else:
        registers[register] = registers[value]
    print("News register %s with the value %s was created" % (register, value))
    print("All registers: " + str(registers))


def inc(register):
    registers[register] = int(registers[register]) + 1
    print("Register %s was increased by 1" % (register))
    print("All registers: " + str(registers))


def dec(register):
    registers[register] = int(registers[register]) - 1
    print("Register %s was decreased by 1" % (register))
    print("All registers: " + str(registers))


def jnz(register, steps, program, commandIndex):
    if register != '0':
        if '-' in steps:
            iterator(program, commandIndex - int(steps[1]))
        else:
            iterator(program, commandIndex + int(steps))
    print("All registers: " + str(registers))
