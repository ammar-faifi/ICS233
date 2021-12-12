# ICS233
some files for the ICS233 course at KFUPM

To simplify converting the instructions into its form in hex values to be used in the ROM instructions,
I created this simple-like assembler program that might speed up writing your test cases.

# IMPORTANT NOTES

- The instructions are as those in the project document, but in lowercase only.
- the labels like `labe:` not supported. you need to specifiy it with signed number, indicating how many instructions to skip.
- You must not exceed the allowed ranges for the imm5 and imm11, you might not be warnned and it will cause wrong hex values.
- You must use one white space, no more.
- Do not use tabs, not supported yet.
- use `$` for register number. i.e., `$0 - $7`.

# Example
```
addi $0, $1, 1
addi $1, $2, 0
imm 1
j -2
```
The out put will be 
```
v2.0 raw
4021
4140
f001
e7fe
```
You can load the output file directly into Logisim now!

# Hoe to Use
- create a file called `input.txt`
- put in the folder with the `assembler.py`
- run the python program normally