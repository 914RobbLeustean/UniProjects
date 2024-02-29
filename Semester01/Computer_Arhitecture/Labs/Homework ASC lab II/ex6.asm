bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
     
    a dw 5
    b dw 3
    c dw 2
    result dw 0  ; Variable to store the result
    
section .text   ; Code section
start:

    mov ax, [a]
    mov bx, [b]
    mov cx, [c]

    
    add bx, cx  ; b + c
    sub bx, ax  ; (b + c) - a

    
    mov [result], bx


    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
