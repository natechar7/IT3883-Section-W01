# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Nathaniel Charles
# Assignment Number: Lab1
# Due Date: 9/22/2026
# Purpose: This program implements a text-based menu that allows a user to
#          append data to an input buffer (a string), clear the buffer,
#          display the buffer's current contents, or exit the program.
#          The menu keeps looping until the user chooses to exit.
# Resources: Python documentation (docs.python.org) for string concatenation and input() usage. No external code was
#            copied.


buffer_text = ""
running = True

    # Main menu loop
while running:
    print("\n===== MENU =====")
    print("1) Add text to buffer")
    print("2) Clear buffer")
    print("3) Show buffer")
    print("4) Exit")

    choice = input("Enter choice (1-4): ")

    # Append new input to the buffer
    if choice == "1":
        new_text = input("Enter text to add: ")
        buffer_text += new_text
        print("Added.")

    # Reset the buffer
    elif choice == "2":
        buffer_text = ""
        print("Buffer cleared.")

    # Print current buffer contents
    elif choice == "3":
        if buffer_text == "":
            print("Buffer is empty.")
        else:
            print("Buffer contents:", buffer_text)

    # Exit the loop and end the program
    elif choice == "4":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice, try again.")