bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
    a db 2 
    b db 3 
    c db 4
    d db 5
    result db 0
    
section .text   ; Code section ; Am avut de rezolvat:(c-a-d)+(c-b)-a (ex5)
start:
    mov AL, [a]
    mov BL, [b]
    mov CL, [c] 
    mov DL, [d]
    
    
    
    sub CL, AL ; c-a
    sub CL, DL; c-a-d
    
    mov CH, CL; CH = c - a - d
    mov CL, [c]; CL = c
    
    sub CL, BL; c-b
    add CH, CL; CH = (c-a-d) + (c-b)
    sub CH, AL; (c-a-d) + (c-b) - a
    
    mov [result], CH;
    
    
    
    
    
    
    
    
    
    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
