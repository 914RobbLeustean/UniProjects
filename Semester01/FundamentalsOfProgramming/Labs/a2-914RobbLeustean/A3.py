import random
import timeit

#Function for random list of n elements
def generate_random_list(n):
    return [random.randint(0, 100) for _ in range(n)]

#Function for Best Case
def generate_best_case_list(n):
    return list(range(1, n + 1)) #Returning  a list from 1 -> n

#Function for Worst Case
def generate_worst_case_list(n):
    return list(range(n, 0, -1)) #Returning a list from 1 -> n but in reverse order

# Function for bubble sort
def bubble_sort(arr):
    n = len(arr) #Taking its length so we know how many iterations need to be done
    for i in range(n): #for each pass the largest unsorted nr gets placed in its position
        for j in range(0, n - i - 1): #n-i-1 means we decrease the iterations by 1 since we moved the biggest element already 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swapping j and j+1 if j+1>j

# Function for stooge sort
def stooge_sort(arr): #arr = list that needs to be sorted
    def stooge(arr, l, h): #we take the list and two indexes to define the sorted range
        if l >= h: #base case, if the lower index is > higher index
            return #it means we only have 1 or 0 elements so no sorting needed
        if arr[l] > arr[h]: #we want to make sure that the element in the lower index
            arr[l], arr[h] = arr[h], arr[l] #is always smaller than the one at the higher index
        if h - l + 1 >= 3: #checking if the nr of elements in [1,h] > 3 so later we can
            t = (h - l + 1) // 3 #divide the list into 3 parts
            stooge(arr, l, h - t) #sorting from l to h-t
            stooge(arr, l + t, h) #sorting from l+t to h
            stooge(arr, l, h - t) #veryfying if all elements are sorted properly
    stooge(arr, 0, len(arr) - 1) 

#Function for performance
def performance_test(sort_func, case):
    durations = [] #storing the durations of different list lengths
    list_lengths = [50, 100, 200, 400]

    for list_length in list_lengths: #we iterate thru each list
        if case == "best":
            input_list = generate_best_case_list(list_length)
        elif case == "worst":
            input_list = generate_worst_case_list(list_length)
        else:
            input_list = generate_random_list(list_length)

        duration = timeit.timeit(lambda: sort_func(input_list[:]), number=1) #timing the execution of the sorting func on a copy of the input list, =1 means we only want to time it once
        durations.append((list_length, duration)) #this contains the sizes and duration

    return durations

#Menu
while True:
    print("\nMenu:")
    print("1. Generate a list of random natural numbers")
    print("2. Sort the list using Bubble Sort")
    print("3. Sort the list using Stooge Sort")
    print("4. Test Bubble Sort - Best Case")
    print("5. Test Bubble Sort - Average Case")
    print("6. Test Bubble Sort - Worst Case")
    print("7. Test Stooge Sort - Best Case")
    print("8. Test Stooge Sort - Average Case")
    print("9. Test Stooge Sort - Worst Case")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter the number of elements: "))
        random_list = generate_random_list(n)
        print("Random list:", random_list)
    elif choice == '2':
        if 'random_list' in locals():
            bubble_sort(random_list)
        else:
            print("Please generate a list first.")
    elif choice == '3':
        if 'random_list' in locals():
            stooge_sort(random_list)
        else:
            print("Please generate a list first.")
    elif choice == '4':
        results = performance_test(bubble_sort, "best")
        for length, duration in results:
            print(f"List Length: {length}, Sort Duration: {duration:.6f} seconds")
    elif choice == '5':
        results = performance_test(bubble_sort, "average")
        for length, duration in results:
            print(f"List Length: {length}, Sort Duration: {duration:.6f} seconds")
    elif choice == '6':
        results = performance_test(bubble_sort, "worst")
        for length, duration in results:
            print(f"List Length: {length}, Sort Duration: {duration:.6f} seconds")
    elif choice == '7':
        results = performance_test(stooge_sort, "best")
        for length, duration in results:
            print(f"List Length: {length}, Sort Duration: {duration:.6f} seconds")
    elif choice == '8':
        results = performance_test(stooge_sort, "average")
        for length, duration in results:
            print(f"List Length: {length}, Sort Duration: {duration:.6f} seconds") 
    elif choice == '9':
        results = performance_test(stooge_sort, "worst")
        for length, duration in results:
            print(f"List Length: {length}, Sort Duration: {duration:.6f} seconds")
    elif choice == '10':
            break
    else:
        print("Invalid statement. Please try agian")   
