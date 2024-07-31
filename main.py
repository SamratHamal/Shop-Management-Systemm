import Operation  # importing operation file
import Write  # importing write file
import read  # importing read file
import random  # importing the built-in module
import datetime  # importing python module


def User_option():
    loop = True
    while loop:
        print("Select your choice ")
        print("Press 1 to Sell: ")
        print("Press 2 for Purchases:")
        print("Press 3 for Exit:")

        loop1 = True
        while loop1:
            try:
                user_ask = int(input("Enter a value to Continue: "))
                loop1 = False
            except ValueError:
                print("Enter a mathematical numeric value")

        print("\n")
        if user_ask > 3:
            print("invalid error ...")
            loop = True
            continue

        if user_ask == 1:
            read.display()  # Call a function display from module read
            print(
                "---------------------------------------------------------------------------------------------------------------------------------------")
            strngloop = True
            while strngloop:
                userName = str(input("Name: "))

                try:
                    if userName.isalpha():  # check if user input contains only alphabetical characters
                        break
                    else:
                        raise ValueError("alphabetical error !!")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    strngloop = False

            strngaloop1 = True
            while strngaloop1:
                Address = str(input("Address: "))

                try:
                    if Address.isalpha():  # check if user input contains only alphabetical characters
                        pass
                    else:
                        raise ValueError("Alphabetical error !!")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    strngaloop1 = False

            numbeloop = True
            while numbeloop:
                try:
                    contactnumber = int(input("Contact Number: "))  # Prompt user to enter a contact number and convert the input to an integer
                    if contactnumber < 0:
                        raise ValueError("Negative error")
                    numbeloop = False  # Exit the loop if user input is a numeric value
                except ValueError:
                    print("Non Numeric error")  # Inform the user that they entered a non-numeric value

            Lst = []  # Initialize an empty list to store the laptop purchases
            while True:
                id = True  # Set id to True to enter the loop for validation of laptop id
                dict = read.myfunction()  # Get the dictionary of available laptops
                while id:
                    laptop_id = Operation.validation_lp_num(dict)  # Validate the entered laptop id
                    print(f"Available stocks {dict[laptop_id][3]} only")  # Display the available stock of the selected laptop
                    if int(dict[laptop_id][3]) == 0:
                        Operation.loop()  # If the stock is 0, prompt the user to try again
                    else:
                        id = False  # Exit the loop if there is stock of the selected laptop
                quantity_of_laptop = Operation.quantity_validation(dict, laptop_id, user_ask)  # Validate the quantity of the selected laptop to be purchased
                if quantity_of_laptop > int(dict[laptop_id][3]):
                    print("Not enough stock available. Please enter a valid quantity.")
                    continue
                dict = Operation.dictionary_update(laptop_id, quantity_of_laptop, Lst)  # Update the dictionary with the purchased quantity of the selected laptop
                Write.update(dict)  # Write the updated dictionary to the file
                loop_1 = True
                while loop_1:  # Loop until the user answers if they want to buy more
                    ask_again = input("Do you want to buy again: ")
                    print("-----------------------------------------------------------------------")
                    if ask_again == 'y':  # If the user wants to buy more
                        loop_1 = False
                    elif ask_again == 'n':  # If the user is done purchasing
                        loop_1 = False
                        break
                    else:  # If the user input is invalid
                        print("Invalid value. Press 'y' for Yes and 'n' for No")

                if ask_again == 'n':
                    break

            bill_no = random.randint(0, 5000)  # Generate a random bill number
            date = datetime.datetime.now().strftime("%d/%m/%Y")  # Get the current date
            time = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current time
            Write.bill(userName, Address, contactnumber, Lst, bill_no, date, time)  # Generate the bill for the laptop purchases
            Write.bill_sell(userName, Address, contactnumber, Lst, bill_no, date, time)  # Generate the sell bill for the laptop purchases
            print("\n")
            print("Thank you for your cooperation.")  # Display the message after the purchase is complete
            print("-" * 150)
            print("\n")

        if user_ask == 2:
            read.display()  # Display the available laptops
            print("------------------------------------------------------------------------------------------------------------------")
            namo=True
            while namo:
                user_name = input("Name: ")
                try:
                    if user_name.isalpha():  # check if user input contains only alphabetical characters
                        break
                    else:
                        raise ValueError("Alphabetical error !!")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    namo = False

            my_dict = read.myfunction()  # Retrieve the dictionary of available laptops
            Lst = []  # Initialize an empty list for the user's purchase history
            while True:  # Loop until the user is done purchasing
                laptop_id = input("Enter the laptop ID you want to buy: ")  # Ask the user to input the laptop ID
                try:
                    laptop_id = int(laptop_id)  # Convert the input to an integer
                    quantity_of_laptop = Operation.quantity_validation(my_dict, laptop_id, user_ask)  # Validate the user's input for quantity
                    if quantity_of_laptop > int(my_dict[laptop_id][3]):
                        print("Not enough stock available. Please enter a valid quantity.")
                        continue
                    my_dict = Operation.dictionary_update_purchase(laptop_id, quantity_of_laptop, Lst)  # Update the dictionary after purchase
                    Write.update(my_dict)  # Write the updated dictionary to the file
                    loop_1 = True
                    while loop_1:  # Loop until the user answers if they want to buy more
                        ask_again = str(input("Do you want to buy again: "))
                        print("-----------------------------------------------------------------------")
                        if ask_again == 'y':  # If the user wants to buy more
                            loop_1 = False
                        elif ask_again == 'n':  # If the user is done purchasing
                            loop_1 = False
                            break
                        else:  # If the user input is invalid
                            print("Invalid value. Press 'y' for Yes and 'n' for No")

                    if ask_again == 'n':
                        break
                except ValueError:
                    print("Invalid laptop ID. Please enter a valid ID.")
                    continue

            bill_no = random.randint(0, 500)  # Generate a random bill number
            date = datetime.datetime.now().strftime("%d/%m/%Y")  # Get the current date
            time = datetime.datetime.now().strftime('%Y/%m/%d %I:%M:%S')  # Get the current time
            Write.biil_purchase(user_name, Lst, bill_no, date, time)  # Write the purchase history to the purchase file
            Write.bill_text_purchases(user_name, Lst, bill_no, date, time)  # Write the purchase history to the text file
            print("\n")
            print("Thank you for your cooperation. Have a good day.")
            print("-" * 150)
            print("\n")

        elif user_ask == 3:
            print("*" * 150)
            print("Exiting the program ...")
            print("Please buy from us again ")
            print("*" * 150)
            loop = False


User_option()
