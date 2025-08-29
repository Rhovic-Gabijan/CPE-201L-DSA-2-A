def main():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(f"\nOriginal Array: {numbers}")

    totoo = True
    while totoo:
        print("""\nMenu:
1. Access individual elements.
2. Compute for the sum.
3. Append new item.
4. Insert new item.
5. Reverse Array.
6. Show Array.
7. Exit""")
    
        choice = int(input("Enter your choice (1-7): "))
    
        if choice == 1:
            Access_elements(numbers)
        elif choice == 2:
            compute(numbers)
        elif choice == 3:
            append_item(numbers)
        elif choice == 4:
            insert_item(numbers)
        elif choice == 5:
            reverse(numbers)
        elif choice == 6:
            show_array(numbers)
        elif choice == 7:
            print("\nExiting the program...")
            totoo = False
        else:
            print("\nInvalid. Choose between 1-7.")
        
def Access_elements(numbers):
        access = int(input("\nEnter Number to Access index: "))
        print(f"Index[{access}]: {numbers[access]}")
        
def compute(numbers):
    print(f"\nSum of Array: {sum(numbers)}")

def append_item(numbers):
    ilagay = int(input("\nEnter Value to append: "))
    numbers.append(ilagay)
    print(f"Value {ilagay} append.")
    
def insert_item(numbers):
    lagay = int(input("\nEnter number to insert: "))
    sanlagay = int(input("Enter Index: "))
    numbers.insert(sanlagay, lagay)
    print(f"Value {lagay} insert to index {sanlagay}.")
    
def reverse(numbers):
    print("\nReversing array: ")
    for i, element in enumerate(reversed(numbers)):
        print(f"Index {len(numbers)-1-i}: {element}")

def show_array(numbers):
    print("List of Array:")
    for i, element in enumerate(numbers):
        print(f"Index[{i}]: {element}")

if __name__ == "__main__":
    main()