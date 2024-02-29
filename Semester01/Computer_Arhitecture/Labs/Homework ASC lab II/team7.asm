bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
    a db 5
    b db 1 
    c db 10
    d dw 4
    result dw 0
    
section .text   ; Code section ;Am avut de rezolvat: [d-2*(a-b)+b*c]/2 (ex5)
start:
    mov AL, [a]
    mov BL, [b]
    mov CL, [c]
    mov DX, [d]
    
    sub AL, BL; a-b
    mov AH,2
    imul AH; (a-b) * 2 <=> AX = AH * AL
    mov BX, AX; BX = AX
    mov AL, [b]
    imul byte [c]; AX = AL * c = b * c 
    add BX,AX; (a-b)+b*c
    sub DX, BX; d-2*(a-b)+b*c
    mov AX, DX
    mov CX, 2
    mov DX, 0
    idiv CX; [d-2*(a-b)+b*c]/2
    
    
    
    
    
   
    
    
    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    