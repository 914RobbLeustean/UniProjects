bits 32         ; Assembling for the 32-bit architecture
global start    ; Declare the 'start' label as the entry point of the program

extern exit     ; Inform the assembler that the 'exit' symbol is external (defined in an external library)
import exit msvcrt.dll  ; Specify that 'exit' is defined in the msvcrt.dll library

section .data   ; Data section
   
   a dw 0101011101010111b
   b dw 1011111010111110b
   c dd 0
    
    
section .text   ; Code section ;
start:
                mov EBX, 0; we clear BX so we can store the result
                or EBX, 00000000000000001111111111111111b; forcing the value of the bits 16-31 to the value 0
                
                mov EAX, [a]; we isolate the bits 3-8 of A
                and EAX, 00000000000000000000000111111000b;
                mov CL, 3
                ror EAX, CL; we rotate 3 positions to the right
                and EBX, EAX; we put the bits into the result
                
                mov EAX, [b]; we isolate the bits 2-4 of B
                and EAX, 00000000000000000000000000011100b
                mov CL, 4
                rol EAX, CL; we rotate 4 positions to the left
                or EBX, EAX; we put the bits into the result
                
                mov EAX, [a]; we isolate the bits 6-12 of A
                and EAX, 00000000000000000001111111000000b
                mov CL, 3
                rol EAX, CL; we rotate 3 positions to the left
                or EBX, EAX; we put the bits into the result
                
                mov [c], EBX; we move the result from the register to the result variable
           

                
                
                

                 
        
      

    ; Call 'exit(0)' to end the program (0 represents a success status)
    push dword 0  ; Push the parameter (status code) onto the stack
    call [exit]   ; Call the 'exit' function to exit the program
    