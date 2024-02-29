bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
   
   a db 5
   b dw 6
   c dd 2
   d dq 10
   
   
    
    
section .text   ; Code section ;Am avut de rezolvat: a-b-(c-d)+d(ex20) a - byte, b - word, c - double word, d - qword - Signed  representation
start:
         mov AL, [a]; AL = a
         cbw; AX = a 
         mov BX, [b]; BX = b 
         sub AX, BX; a - b 
         mov CX, AX; CX = a - b 
         mov EAX, [c]; EAX = c 
         cdq; EAX -> EDX:EAX 
         sub EAX, [d]; EAX =  c - d 
         mov EBX, EAX; EBX = EAX
         mov AX, CX; AX = CX 
         cwde; AX -> EAX 
         cdq; EAX -> EDX:EAX
         sub EAX, EBX; a-b-(c-d)
         
         
            
            
            
            
            
      

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    