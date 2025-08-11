def main():
    arr = [40, 10, 50, 20, 30]
    print(f"\nOriginal array: {arr}")
    
    x = True
    while x:
        print("""\nMenu:
1. Traverse array
2. Reverse array
3. Sort Array
4. Modify Array
5. Exit""")
        choice = int(input("Enter your choices (1-5): "))
        
        if choice == 1:
            traverse_array(arr)
        elif choice == 2:
            reverse(arr)
        elif choice == 3:
            sort(arr)
        elif choice == 4:
            modify(arr)
        elif choice == 5:
            print("\nExiting the program...")
            x = False
        else:
            print("\nInvalid Choice. Choose between 1-5.")
            print("-"*25)
            
def traverse_array(arr):
    print("\nTraversing the array: " )
    for i, element in enumerate(arr):
        print(f"Index {i}: {element}")
    print("-"*25)
    
def reverse(arr):
    print("\nreversing all elements")
    for i, element in enumerate(reversed(arr)):
        print(f"Index {len(arr)-1-i}: {element}")
    print("-"*25)    
    
def sort(arr):
    print("\nSorting the array: ")
    sorted_arr = sorted(arr)
    for i, element in enumerate(sorted_arr):
        print(f"Index {i}: {element}")
    print("-"*25)
  
def modify(arr):
    totoo = True
    while totoo:
        print("""\nModifying array. Choose number to Modify.
1. Append
2. Delete
3. Done""")
        pinili = int(input("Enter your Choice: "))
    
        if pinili == 1:
            value = int(input("Enter value to insert: "))
            arr.append(value)
            print(f"Value {value} added.")
            print("-"*25)
            totoo = False
            
        elif pinili == 2:
            index = int(input("Enter index to delete: "))
            if 0 <= index < len(arr):
                removed = arr.pop(index)
                print(f"Value {removed} removed from index {index}.")
                totoo = False
            else:
                print("Invalid index.")
            print("-"*25)
            
        elif pinili == 3:
            print("\nDone")
            print("-"*25)
            totoo = False
        else:
            print("Invalid Choice. Choose between 1 to 3")
            print("-"*25)
        
if __name__ == "__main__":
    main()