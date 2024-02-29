

bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
    a db 5
    b db 1 
    c db 10
    d db 4
    g dw 12
    
    
section .text   ; Code section ;Am avut de rezolvat: [(a+b+c)*2]*3/g (ex20)
start:
      mov AL, [a]
      add AL, byte [b]; a + b 
      add AL, byte [c]; a + b + c 
      mov AH, 2
      imul AH; AX = AL * AH = (a+b+c)*2
      mov DX, 3
      mul DX; DX:AX = AX * DX = [(a+b+c)*2] * 3
      mov CX, [g]
      idiv CX; AX = DX:AX / CX = [(a+b+c)*2] * 3 / g 