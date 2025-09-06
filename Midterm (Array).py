import array as arr

def main():
    arr.typecodes
    num = arr.array('i', [i for i in range(20, 50) if i % 2 == 0])
    print(num)
    x = True
    while x:
        print("""\nMenu:
1. Display Even Numbers.
2. Display Maximum Number.
3. Display Minimum Number.
4. Reverse Array.
5. Exit.""")       
        choice = int(input("Enter your Choice (1-5): "))
        if choice == 1:
            display_even(num)
        elif choice == 2:
            display_max(num)
        elif choice == 3:
            display_min(num)
        elif choice == 4:
            reverse_array(num)
        elif choice == 5:
            print("\nExiting the program...")
            x = False
        else:
            print("Invalid Choice. Choose between 1-5.")
            
def display_even(num):
    print("\nEven Numbers in the Array: ")
    for n in num:
        if n % 2 == 0:
            print(n)
            
def display_max(num):
    if len(num) == 0:
        print("Array is empty. No maximum value.")
    else:
        max_num = num[0]
        for i in num:
            if i > max_num:
                max_num = i
        print(f"\nMaximum Number in the Array: {max_num}")

def display_min(num):
    if len(num) == 0:
        print("Array is empty. No minimum value.")
    else:
        min_num = num[0]
        for i in num:
            if i < min_num:
                min_num = i
        print(f"\nMinimum Number in the Array: {min_num}")
        
def reverse_array(num):
    print("\nArray in Reverse Order: ")
    for i in range(len(num)-1, -1, -1):
        print(num[i])
        
if __name__ == "__main__":
    main()