from radix import Bin

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


def binf(num: str, fill: int):
    return str(bin(int(num))[2:]).zfill(fill)


with open("input.txt", "r") as file:
    lines = file.readlines()
    count = 0

    for line in lines:
        op = line.rstrip("\n").split(" ")[0]
        count += 1

        if op in R:
            op, a, b, d = line.rstrip("\n").split(" ")

            f = str(bin(R.get(op)[1])[2:]).zfill(2)
            op = str(bin(R.get(op)[0])[2:]).zfill(5)
            a = binf(a[1:2], 3)
            b = binf(b[1:2], 3)
            d = binf(d[1:2], 3)

            inst = f"{op}{a}{b}{d}{f}"
            inst_hex = hex(int(inst, 2))
            OUT.append(inst_hex + "\n")

        elif op in I:
            op, a, b, imm = line.rstrip("\n").split(" ")

            op = str(bin(I.get(op))[2:]).zfill(5)
            a = binf(a[1:2], 3)
            b = binf(b[1:2], 3)
            imm = Bin(imm).format(5)

            inst = f"{op}{a}{b}{imm}"
            inst_hex = hex(int(inst, 2))
            OUT.append(inst_hex + "\n")

        elif op in J:
            op, imm = line.rstrip("\n").split(" ")

            op = str(bin(J.get(op))[2:]).zfill(5)
            imm = Bin(imm).format(11)

            inst = f"{op}{imm}"
            inst_hex = hex(int(inst, 2))
            OUT.append(inst_hex + "\n")

        else:
            exit(f"Error: `{op}` is not recognizable in line {count}")


try:
    with open("output.txt", "w") as file:
        file.write("v2.0 raw\n")
        for line in OUT:
            file.write(line[2:].zfill(5))
    print("DONE")

except FileExistsError:
    print("ERROR: It seems there is a file has the exact name")
