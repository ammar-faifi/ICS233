import sys
import os
from radix import Bin, Num

R = {
    "and": (0, 0),
    "cand": (0, 1),
    "or": (0, 2),
    "xor": (0, 3),
    "add": (1, 0),
    "nadd": (1, 1),
    "seq": (1, 2),
    "slt": (1, 3),
}
I = {
    "andi": 4,
    "candi": 5,
    "ori": 6,
    "xori": 7,
    "addi": 8,
    "naddi": 9,
    "seqi": 10,
    "slti": 11,
    "sll": 12,
    "srl": 13,
    "sra": 14,
    "ror": 15,
    "beq": 16,
    "bne": 17,
    "blt": 18,
    "bge": 19,
    "lw": 20,
    "sw": 21,
    "jalr": 27,
}
J = {
    "j": 28,
    "jal": 29,
    "imm": 30,
}

OUT = []

with open("assembler/example.txt", "r") as file:
    lines = file.readlines()
    count = 0

    for line in lines:
        op = line.removesuffix("\n").split(" ")[0]
        count += 1

        if op in R:
            op, a, b, d = line.removesuffix("\n").split(" ")
            # f = str(bin(R.get(op)[1])[2:]).zfill(2)
            # op = str(bin(R.get(op)[0])[2:]).zfill(5)
            f = str(bin(R.get(op)[1])[2:]).zfill(2)
            op = str(bin(R.get(op)[0])[2:]).zfill(5)
            a = str(bin(int(a[1:2]))[2:]).zfill(3)
            b = str(bin(int(b[1:2]))[2:]).zfill(3)
            d = str(bin(int(d[1:2]))[2:]).zfill(3)
            inst = f"{op}{a}{b}{d}{f}"
            inst_hex = hex(int(inst, 2))
            OUT.append(inst_hex + "\n")

        elif op in I:
            op, a, b, imm = line.removesuffix("\n").split(" ")
            # op = Bin(I.get(op)).format(5)
            op = str(bin(I.get(op))[2:]).zfill(5)
            a = Bin(a[1:2]).format(3)
            b = Bin(b[1:2]).format(3)
            imm = Bin(imm).format(5)
            inst = f"{op}{a}{b}{imm}"
            inst_hex = hex(int(inst, 2))
            OUT.append(inst_hex + "\n")

        elif op in J:
            op, imm = line.removesuffix("\n").split(" ")
            # op = Num(J.get(op)).to(2)
            op = str(bin(J.get(op))[2:]).zfill(5)
            imm = Bin(imm).format(11)
            inst = f"{op}{imm}"
            inst_hex = hex(int(inst, 2))
            OUT.append(inst_hex + "\n")

        else:
            exit(f"Error: `{op}` is not recognizable in line {count}")

print(OUT)

try:
    with open("assembler/output.txt", "w") as file:
        file.write("v2.0 raw\n")
        for line in OUT:
            file.write(line[2:])

except FileExistsError:
    print("ERROR: It seems there is a file has the exact name")
