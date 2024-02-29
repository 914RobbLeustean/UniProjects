;A character string S is given. Obtain the string D containing all small letters from the string S.
bits 32 
global start        
extern exit; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll ; exit is a function that ends the calling process. It is defined in msvcrt.dll
; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
; our data is declared here (the variables needed by our program)

segment data use32 class=data
	s db 'a', 'A', 'b', 'B', '2', '%', 'x' ; declare the string of bytes
	l equ $-s ; compute the length of the string in l
	d times l db 0 ; reserve l bytes for the destination string and initialize it
    
segment code use32 class=code
start:
	mov ecx, l ; we put the length l in ECX in order to make the loop
	mov esi, 0
    mov edi, d
    
	jecxz Sfarsit      
	Repeta: ;Syntax for a loop function, <label>;, then below it we add operations / code to execute
		mov al, [s+esi]; loading a character from string S into AL
		
        cmp al, 'a'; character small than a so it's not lowercase
        jl  not_lower
        cmp al, 'z'; character higher than z so it's not lowercase
        jg not_lower
        
		mov [edi], al; store lowercase character in string D
		inc edi; move to the next position in the string D
    
    not_lower:
        inc esi  ; move to the next character in string S
        ;jmp Repeta ; continue checking characters
        
    loop Repeta; loop <label>; we are telling the program to go back and execute as long as ECX is not zero !!
	Sfarsit: ; ECX is zero so that means we jump here and don't execute any more lines of code
	; exit(0)
	push dword 0 ; push the parameter for exit onto the stack
	call [exit] ; call exit to terminate the program