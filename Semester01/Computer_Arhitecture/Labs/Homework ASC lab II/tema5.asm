bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
    a dw 2 
    b dw 3 
    c dw 10
    d dw 5
    result dw 0
    
section .text   ; Code section ;Am avut de rezolvat:(c+b+b)-(c+a+d) (ex5)
start:
    mov AX, [a]
    mov BX, [b]
    mov CX, [c] 
    mov DX, [d]
    
    
    add BX, BX; b+b
    add CX, BX; c + b + b
    mov BX, CX; BX = c + b + b
    mov CX, [c]; CX = c 
    add CX, AX; c + a
    add CX, DX; c + a + d 
    sub BX, CX; (c+b+b)-(c+a+d)
    mov [result], BX
    
   
    
    
    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    