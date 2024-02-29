bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions





segment data use32 class=data
    s1 db 7, 33, 55, 19, 46   ; s1 byte string
    s2 db 33, 21, 7, 13, 27, 19, 55, 1, 46   ; s2 byte string
    s1_len equ $ - s1          ; length of s1
    s2_len equ $ - s2          ; length of s2
    result db s2_len    ; result string initialized 

segment code use32 class=code
    start:
        mov ecx, s2_len
        mov ebx, 0
        mov esi, 0
        
        
        
        
        
    
    
    
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
    ; Your code to handle the result goes here
    ; The result is stored in the "result" variable
    ; You can print it, store it, or perform any other operations needed
