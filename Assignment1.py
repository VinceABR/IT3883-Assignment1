# Student Name: Vince Abraham
# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Assignment Number: Assignment 1
# Due Date: 09/22/2026
# Purpose: This program creates a text-based menu that allows the user
# to add text to an input buffer, clear the buffer, display its current
# contents, or exit the program.
# Resources Used: Assignment 1 instructions
# Create an empty string to store the user's input
input_buffer = ""
# Keep displaying the menu until the user chooses to exit
while True:
    print("\n--- Input Buffer Menu ---")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")
    menu_choice = input("Enter your choice (1-4): ")

    # Option 1 adds new text to the existing buffer
    if menu_choice == "1":
        new_text = input("Enter a string to append: ")
        input_buffer += new_text + " "
        print("Data added to the input buffer.")

    # Option 2 removes everything currently stored
    elif menu_choice == "2":
        input_buffer = ""
        print("Input buffer cleared.")

    # Option 3 displays the current contents of the buffer
    elif menu_choice == "3":
        print("Current input buffer:", input_buffer)

    # Option 4 ends the program
    elif menu_choice == "4":
        print("Exiting program.")
        break

    # Handle anything other than choices 1 through 4
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")