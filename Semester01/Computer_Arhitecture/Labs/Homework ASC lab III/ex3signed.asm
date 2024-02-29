bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
   
   a dd 5
   b db 6
   c dw 2
   x dq 10
   
   
    
    
section .text   ; Code section ;Am avut de rezolvat: (a+b/c-1)/(b+2)-x (ex5) ; a-doubleword; b-byte; c-word; x-qword
start:
        sub word [c], 1; c = c - 1
        mov AL, [b]
        cbw; AX = AL 
        add AX, [a];AX = a + b 
        mov CX, [c]; CX = c 
        mov DX, 0
        div CX; AX = (a+b) / c - 1 ; DX = (a+b) % c - 1
        add byte [b], 2; b = b + 2
        mov BX, AX; BX = AX 
        mov AL, [b]
        cbw; AX = AL
        mov CX, AX; CX = AX
        mov AX, BX; BX = AX
        div CX; AX = (a+b/c-1)/(b+2)
        cwde; AX -> EAX
        cdq; EAX -> EDX:EAX
        sub EAX, [x];
        



        

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    