# ICS233 Simple Assembler

some files for the ICS233 course at KFUPM

To simplify converting the instructions into its form in hex values to be used in the ROM instructions,
I created this simple-like assembler program that might speed up writing your test cases.

## IMPORTANT NOTES

- The instructions are as those in the project document, but in lowercase only.
- the labels like `labe:` not supported. you need to specifiy it with signed number, indicating how many instructions to skip.
- You must not exceed the allowed ranges for the imm5 and imm11, you might not be warnned and it will cause wrong hex values.
- You must use one white space, no more.
- Do not use tabs, not supported yet.
- use `$` for register number. i.e., `$0 - $7`.

## How to Use

- Clone this project or just download the `assembler.py` file.
- You should have python3 installed.
- You need to install the lib `radix-ops`, by writing in the command line `pip install radix-ops`
- Create a file called `input.txt`, contains your instructions.
- Put it in the same folder with the `assembler.py`.
- Run the python program normally, `python3 assembler.py`
- It will create `output.txt`.

## Example

```txt
addi $0, $1, 1
addi $2, $2, 1
imm 1
j -2
```

The out put will be

```txt
v2.0 raw
4021
4241
f001
e7fe
```

You can load the output file directly into Logisim now!
