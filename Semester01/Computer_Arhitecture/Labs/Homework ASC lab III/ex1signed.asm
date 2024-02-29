bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
   
   a db 5
   b dw 6
   c dd 2
   d dq 10
   
   
    
    
section .text   ; Code section ;Am avut de rezolvat: (c+b+b)-(c+a+d)(ex5) a - byte, b - word, c - double word, d - qword - Signed  representation
start:
         mov AX, [b]; AX = b 
         add AX, [b]; AX = b + b
         cwde; Storing the result from AX into EAX
         mov EBX, [c]
         add EAX, EBX; EAX = c + b + b
         mov  EBX, EAX; EBX = EAX
         mov AL, [a]
         cbw; Storing the result form AL into AX 
         cwde; Storing the result from AX into EAX
         add EAX, [c]; EAX = c + a 
         cdq; Storing the result from EAX into EDX;EAX 
         add EAX, [d]; EDX = c + a + d 
         sub EBX, EAX; (c+b+b)-(c+a+d)
         
         
         
            
            
            
            
            
      

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    