bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
     
    a db 5
    b db 3
    c db 8
    d db 2
    result db 0   
    
section .text   
start:

    
    mov al, [a]
    mov bl, [b]
    mov cl, [c]
    mov dl, [d]

    
    sub cl, al  ; c - a
    sub cl, dl  ; (c - a) - d
    sub cl, bl  ; ((c - a) - d) - b
    sub al, cl  ; (((c - a) - d) - b) - a

    
    mov [result], al

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
