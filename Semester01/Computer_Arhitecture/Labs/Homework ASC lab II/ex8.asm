bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
     
    a db 5
    b db 3
    cc db 2
    d dw 10
    result dw 0  ; Variable to store the result
    
section .text   ; Code section
start:
    mov al, [a]
    mov bl, [b]
    mov cl, [cc]
    movzx edx, word [d]  

    
    sub ax, bx  ; a - b
    imul ax, ax, 2  ; 2 * (a - b)
    add ax, bx     ; (2 * (a - b)) + b
    imul ax, cl  ; (2 * (a - b) + b) * c
    sub edx, eax   ; d - ((2 * (a - b) + b) * c)

    shr edx, 1    ; (d - 2 * (a - b) + b * c) / 2

    mov [result], dx

    


    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
