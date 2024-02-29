bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
   
   a db 01010111b
   b db 10111110b
   c dd 0
   
   ;the bits 16-31 of C have the value 1
   ;the bits 0-3 of C are the same as the bits 3-6 of B
   ;the bits 4-7 of C have the value 0
   ;the bits 8-10 of C have the value 110
   ;the bits 11-15 of C are the same as the bits 0-4 of A
    
    
section .text   ; Code section ;
start:
                mov EBX, 0; we clear BX so we can store the result
                or EBX, 11111111111111110000000000000000b; forcing the value of the bits 16-31 to the value 1
                
                mov EAX, [b]; we isolate the bits 3-6 of B
                and EAX, 00000000000000000000000001111000b;
                mov CL, 3
                ror EAX, CL; we rotate 3 positions to the right
                or EBX, EAX; we put the bits into the result
                
                and EBX, 11111111111111111111111100001111b; facem biti 4-7 sa aibe valoarea 0
                
                or EBX,  00000000000000000000001100000000b; facem bitii 8-9 sa aibe valoarea 1
                
                and EBX, 11111111111111111111101111111111b; facem bitul 10 sa aibe valoarea 0
                
                mov EAX, [a]; we isolate the bits 0-4 of A 
                and EAX, 00000000000000000000000000011111b
                mov CL, 11
                rol EAX, CL; we rotate 11 positions to the left
                or EBX, EAX; we put the bits into the result
                
                mov [c], EBX; we move the result from the register to the result variable
           

                
                
                

                 
        
      

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    