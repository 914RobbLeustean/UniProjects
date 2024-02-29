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
            
        mov BL, [b]
        mov BH, 0; BX = b 
        mov AL, 2
        mul word [a]; AX = a * 2
        sub AX, BX; 2*a - b 
        mov CX, AX; CX = 2*a - b  
        mov AL, [b]
        mul byte [b]; AX = b * b
        mov BX, AX; BX = b * b 
        mov AX, CX; AX = 2*a - b
        mov DX,0
        DIV BX;
        add byte [b], 8; b = b + 8
        mov BL, [b]
        mov [a], AL; a = (2*a-b)/(b*b)
        add AL, BL; b+8+(2*a-b)/(b*b)
        mov AH, 0;
        mov AX, [a]; a = b+8+(2*a-b)/(b*b)
        mov DX, 0
        mov EAX, [a]; EAX = b+8+(2*a-b)/(b*b)
        mov EDX, 0
        mov EBX, [x]; EBX = x  
        sub EAX, EBX;EAX = x-b+8+(2*a-b)/(b*b)+e
        mov [x], EAX; x = x-b+8+(2*a-b)/(b*b)+e
        mov EAX, [e]
        mov EDX, 0
        add EAX, [x]; EAX = x-b+8+(2*a-b)/(b*b)+e
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
      
      
      
      
      

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    