bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
    a dw 2 
    b dw 3 
    c dw 10
    result dw 0
    
section .text   ; Code section ;Am avut de rezolvat: b-(b+c)+a (ex20)
start:
    mov AX, [a]
    mov BX, [b]
    mov CX, [c] 
    
    
    add BX, CX; b + c 
    mov DX, BX; DX = b + c
    mov BX, [b]
    sub BX, DX; b - (b + c)
    add BX, AX; b-(b+c)+a
    
    mov [result], BX
    
   
    
    
    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    