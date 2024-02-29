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
    
section .text   ; Code section ;Am avut de rezolvat: (50-b-c)*2+a*a+d (ex20)
start:
    mov DX, [d]
    
    mov BL, 50; BL = 50
    sub BL, [b]; 50 - b
    sub BL, [c]; 50 - b - c
    mov AL, BL; AL = 50 - b - c
    mov AH,2
    imul AH; AX = 2*(50 - b - c)    
    mov BX, AX; BX = 2*(50 - b - c)
    mov AH, [a]
    mov AL, [a]
    imul AH; AX = a * a
    add AX, BX; 2*(50 - b - c) + a*a
    add AX, DX; (50-b-c)*2+a*a+d 
    
    
     

   
    
    
    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    