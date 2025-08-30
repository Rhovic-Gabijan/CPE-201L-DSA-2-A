import array as arr

def main():
    arr.typecodes
    name = arr.array('u', [])
    x = True
    while x:
        print("""\nMenu:
1. Input Letter.
2. Traverse Array.
3. Length of Array.
4. Horizontal Name.
5. Exit.""")
        choice = int(input("Enter your Choices (1-5): "))
        if choice == 1:
            input_letter(name)
        elif choice == 2:
            traverse_array(name)
        elif choice == 3:
            array_length(name)
        elif choice == 4:
            horizontal_line(name)
        elif choice == 5:
            print("\nExiting the program...")
            x = False
        else:
            print("Invalid Choice. Choose between 1-5.")

def input_letter(name):
    totoo = True
    while totoo:
        ilagay = input("""\nEnter Letter to add
(Type Quit to stop adding letters): """)
        if ilagay == "Quit":
            print("Word 'Quit' detected. Exiting input loop.")
            totoo = False
            print("-"*25)
        else:
            name.append(ilagay)
            print(f"Letter {ilagay} added.")
        
def traverse_array(name):
    print("\nName: ")
    for i, element in enumerate(name):
        print(element)
def array_length(name):
    print(f"\nLength of array: {len(name)}")
    
def horizontal_line(name):
    print(f"\nName in Horizontal Line: {''.join(name)} ")

if __name__ == "__main__":
    main()
#for i in name:
#    print(i)