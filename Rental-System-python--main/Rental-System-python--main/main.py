# main.py

# Import necessary modules
import operations
import read_file

# Function to display the main menu
def show_menu():
    print("\n")
    # Border
    print("*" * 106)
    # Empty space
    print("| \t \t \t \t \t \t \t \t \t \t \t \t \t |")
    # Welcome message
    print("|\t \t \t      Welcome to Techno Property Nepal Pvt. Ltd   \t\t\t \t |")
    # Empty space
    print("| \t \t \t \t \t \t \t \t \t \t \t \t \t |")
    # Border
    print("*" * 106)
    # Empty space
    print("| \t \t \t \t \t \t \t \t \t \t \t \t \t |")
    # Address and contact information
    print("|\t \t \t Address: Kamalpokhari, Kathmandu | Contact: 9843685535 \t \t \t |")
    # Empty space
    print("| \t \t \t \t \t \t \t \t \t \t \t \t \t |")
    # Border
    print("*" * 106)
    print("\n")
    # Separator
    print("=" * 106)
    print("\n")
    # Instruction for user to select an option
    print("# ------------------- Select any option for further process --------------------------------------\n")
    # Border
    print("*" * 106)
    # Menu options
    print("|                                                                                                        |")
    print("|                          Press 1 to Rent Land                                                          |")
    print("|                                                                                                        |")
    print("|                          Press 2 to Return Land.                                                       |")
    print("|                                                                                                        |")
    print("|                          Press 3 to Exit from the system.                                              |")
    print("|                                                                                                        |")
    # Border
    print("*" * 106)
    print("\n")

# Main function to run the program
def main():
    # Load land data from file
    lands = read_file.load_lands()
    if not lands:
        return

    # Keep showing the menu until the user decides to exit
    while True:
        show_menu()
        choice = input('Choose an option (1-3): ')
        if choice == '1':
            # Rent land
            operations.rent_land(lands, direct_process=True)
        elif choice == '2':
            # Return land
            operations.return_land(lands, direct_process=True)
        elif choice == '3':
            # Exit the system
            print('Thank you for using our system.')
            break
        else:
            # Handle invalid menu choice
            print('Invalid option. Please try again.')

# Start the program
if __name__ == "__main__":
    main()
