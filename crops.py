from wheat_class import *
from potato_class import *

def display_menu():
    print()
    print("WHich crop would you like to create?")
    print()
    print("1. Potateo")
    print("2. Wheat")
    print()
    print("Please Select an Option")

def select_option():
    Valid = False
    while not Valid:
        try:
            choice = int(input("option selected: "))
            if choice in (1,2):
                Valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potateo()
    elif chocie == 2:
        new_crop = Wheat()
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
    
