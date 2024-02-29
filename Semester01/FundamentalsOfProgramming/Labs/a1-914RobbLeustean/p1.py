   # Solve the problem from the first set here

def MaxNumber(n):
   
    num_str = str(n)  #Making the number into a string so we can read it

    sorted_str = ""
    sorted_list = sorted(num_str, reverse=True) #Sorting the list in descending order
    for element in sorted_list:
      sorted_str = sorted_str + element #Making everything into a string one by one

    
    largest_number = int(sorted_str) #We convert the number back to int

    return largest_number

print(MaxNumber(3658))

         
         



