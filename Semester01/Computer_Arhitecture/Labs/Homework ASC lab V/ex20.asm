;Two byte strings A and B are given. Obtain the string R that contains only the even negative elements of the two strings.
;A: 2, 1, 3, -3, -4, 2, -6
;B: 4, 5, -5, 7, -6, -2, 1
;R: -4, -6, -6, -2
bits 32 
global start        
extern exit; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll ; exit is a function that ends the calling process. It is defined in msvcrt.dll
; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
; our data is declared here (the variables needed by our program)

segment data use32 class=data
	A db 2, 1, 3, -3, -4, 2, -6 ; declare the string of bytes
    alen equ $-A; length of A
    B db 4, 5, -5, 7, -6, -2, 1
    blen equ $-B;
    rlen equ alen + blen
	r times alen db 0 ; reserve l bytes for the destination string and initialize it
    
segment code use32 class=code
start:
	mov ecx, alen ; we put the length l in ECX in order to make the loop
	mov esi, 0
    mov edi, r
    
    jecxz Sfarsit
    Repeta:
        mov al, [A+esi]
        test al, 1; check if it's odd 
        jnz next_A; if it's odd we skip
           
        cmp al, 0
        jge next_A;
           
        mov [edi], al
		inc edi
           
    next_A:
        inc esi; move to the next element
    loop Repeta; 
    Sfarsit:
    
    mov ecx, blen ; we put the length l in ECX in order to make the loop
	mov esi, 0
    
    jecxz Sfarsit2
    Repeta2:
        mov al, [B+esi]
        test al, 1; check if it's odd 
        jnz next_B; if it's odd we skip
           
        cmp al, 0
        jge next_B;
           
        mov [edi], al
		inc edi
           
    next_B:
        inc esi; move to the next element
    loop Repeta2; 
    Sfarsit2:

    
	
	; exit(0)
	push dword 0 ; push the parameter for exit onto the stack
	call [exit] ; call exit to terminate the program
