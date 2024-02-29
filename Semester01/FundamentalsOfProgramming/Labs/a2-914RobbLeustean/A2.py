import random

#Genarate random list of n
def generate_random_list(n):
    return [random.randint(0, 100) for _ in range(n)]

#Bubble Sort
def bubble_sort(arr, step):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            if (j + 1) % step == 0 or j == n - i - 2:
                print(f"Step {j + 1}: {arr}")
        if not swapped:
            break

#Stooge Sort
def stooge_sort(arr, step):
    def stooge(arr, l, h):
        if l >= h:
            return
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]
        if h - l + 1 >= 3:
            t = (h - l + 1) // 3
            stooge(arr, l, h - t)
            stooge(arr, l + t, h)
            stooge(arr, l, h - t)
        if (h - l + 1) >= step:
            print(f"Step {h - l + 1}: {arr}")
    stooge(arr, 0, len(arr) - 1)

#Menu
while True:
    print("\nMenu:")
    print("1. Generate a list of random natural numbers")
    print("2. Sort the list using Bubble Sort")
    print("3. Sort the list using Stooge Sort")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter the number of elements: "))
        random_list = generate_random_list(n)
        print("Random list:", random_list)
    elif choice == '2':
        if 'random_list' in locals():
            step = int(input("Enter the step value for Bubble Sort: "))
            bubble_sort(random_list[:], step)
        else:
            print("Please generate a list first.")
    elif choice == '3':
        if 'random_list' in locals():
            step = int(input("Enter the step value for Stooge Sort: "))
            stooge_sort(random_list[:], step)
        else:
            print("Please generate a list first.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")
