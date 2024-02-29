bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
   
   b db 2
   e dd 8
   a dw 12
   x dq 10
   
   
    
    
section .text   ; Code section ;Am avut de rezolvat: x-b+8+(2*a-b)/(b*b)+e (ex20); a-word; b-byte; e-doubleword; x-qword
start:
           mov AL, [b]; AL = b
           mul byte[b]; AX = b * b
           mov CX, AX; CX = AX
           
           mov AL, 2
           mul word[a]; AX = a * 2
           cwde; AX -> EAX
           mov EBX,EAX; EBX = 2 * a 
           
           mov AL, [b]; AL = b
           cbw; AL -> AX, AX = b
           cwde; AX -> EAX, EAX = b
           
           sub EBX, EAX; EBX = 2*a - b
           
           mov AX, CX; AX = CX, AX = b * b
           cwde; AX -> EAX, EAX = b * b
           
           mov ECX, EAX; ECX = EAX, ECX = b * b
           mov EAX, EBX; EAX = EBX, EAX = 2*a - b
           mov EDX, 0
           div ECX; AX = (2*a-b) / b*b
           
           mov CX, AX; BX = (2*a-b) / b*b
           
           add byte[b], 8; b =  b + 8
           mov AL, [b]
           cbw; AL -> AX
           cwde; AX -> EAX
           cdq; EAX -> EDX:EAX
           
           mov EBX, [x]; EBX = x
           sub EBX, EAX; EBX = x - b + 8
           
           mov AX, CX; AX = (2*a-b) / b*b
           cwde; AX - > EAX
           cdq; EAX -> EDX:EAX
           
           add EBX, EAX; EBX = x-b+8+(2*a-b)/(b*b)
           
           mov EAX, [e]; EAX = e 
           cdq; EAX -> EDX:EAX
           add EAX, EBX; EAX = x-b+8+(2*a-b)/(b*b)+e
      

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    