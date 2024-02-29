bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
    result db 0 
    
section .text   ; Code section Am avut de rezolvat: 10/4 (ex5)
start:
    mov AX, 10
    mov BX, 4
    mov DX, 0
    div BX
    mov [result], AL
    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
