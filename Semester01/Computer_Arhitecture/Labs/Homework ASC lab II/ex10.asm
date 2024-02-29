bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
     
    a db 5
    b db 3
    c db 2
    g dw 10
    result dw 0  ; Variable to store the result
    
section .text   ; Code section
start:
   mov al, [a]
    mov bl, [b]
    mov cl, [c]
    movzx dx, word [g]  

    
    add al, bl  ; a + b
    add al, cl  ; (a + b) + c
    imul al, 2  ; (a + b + c) * 2
    imul ax, al, 3  ; [(a + b + c) * 2] * 3
    idiv dx  ; [(a + b + c) * 2 * 3] / g

    
    mov [result], ax
    
    


    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
