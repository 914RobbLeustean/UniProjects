bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
    a db 2 
    b db 3 
    c db 10
    d db 5
    result db 0
    
section .text   ; Code section ;Am avut de rezolvat:(a+a)-(c+b+d) (ex20)
start:
    mov AL, [a]
    mov BL, [b]
    mov CL, [c] 
    mov DL, [d]
    
    
    add CL, BL; c + b
    add CL, DL; c + b + d
    add AL, AL; a + a
    sub AL, CL; (a+a)-(c+b+d)
    
     mov [result], AL;
    
    
    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    