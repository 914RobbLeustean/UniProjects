bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
    a db 5
    b db 1 
    c db 10
    d db 4
    result db 0
    
section .text   ; Code section ;Am avut de rezolvat: a*(b+c)+34 (ex5)
start:
      mov BL, [b]
      add BL, byte [c]; b + c 
      mov AH, BL; AH = b + c 
      mov AL, [a]
      imul AH; a * (b+c)
      add AX, 34; a*(b+c) + 34
    

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    