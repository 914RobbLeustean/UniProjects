bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
   
   a db 5
   b dw 6
   c dd 2
   d dq 10
   
   
    
    
section .text   ; Code section ;Am avut de rezolvat: (c-a-d)+(c-b)-a (ex5) a - byte, b - word, c - double word, d - qword Unsigned
start:
            mov AX, [b]
            mov DX, 0
            mov CX, [c]
            sub CX, AX; c - b 
            mov AL, [a]
            mov AH, 0
            mov DX, 0
            sub CX, AX; c - b - a
            
            mov AL, [a]
            mov AH, 0
            mov DX, 0
            sub [c], AX; c - a 
            mov EAX, [c]
            mov EDX, 0
            sub EAX, [d]; c - a - d
            
            mov [b], CX
            mov ECX, [b]
            add EAX, ECX
            
            
      
      
      
      
      

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    