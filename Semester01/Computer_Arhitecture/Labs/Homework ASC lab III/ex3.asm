bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
   
   b db 9
   c dw 8
   a dd 5
   x dq 10
   
   
    
    
section .text   ; Code section ;Am avut de rezolvat: (a+b/c-1)/(b+2)-x (ex5) ; a-doubleword; b-byte; c-word; x-qword
start:
            mov AL, [b]
            mov AH, 0
            mov DX, 0
            add AX, [a]; DX = a + b 
            adc DX, 1; added line
            sub word [c], 1; c = c - 1
            mov CX, [c]
            div CX; AX = (a+b) / c - 1, DX = (a+1) % c - 1
            add byte [b], 2; b = b + 2
            mov EAX, 0
            mov AL, [b]
            mov AH, 0
            mov DX, 0
            div BX; AX = a+b/c-1)/(b+2), DX = (a+b/c-1) % b + 2
            mov [b], AX
            mov EAX, [b]
            mov EDX, 0
            sub EAX, [x]
            sbb EDX, [x+4]; store the result in EDX:EAX
            
            
            
            
            
            
            
            
            
            
      
      
      
      
      

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    