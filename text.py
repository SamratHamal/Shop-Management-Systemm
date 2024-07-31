import datetime
import random

import Operation
import Write
import read


def User_option():
    loop = True
    while loop == True:
        print("Select your choice ")
        print("press 1 to Sell: ")
        print("press 2 for Purchases:")
        print("Press 3 for Exit:")
        loop1 = True

        while loop1:
            try:
                user_ask = int(input("Enter a value to Continue: "))
            except ValueError as e:
                print("Enter a mathematical numeric value")
            else:
                loop1 = False
        print("\n")
        if user_ask == 1:
            read.display()  # Call a function display from module read
            print(
                "---------------------------------------------------------------------------------------------------------------------------------------")
            loop = True
            strngloop = True
            while strngloop:
                userName = str(input("Name : "))

                try:
                    if userName.isalpha():  # check if user input contains only alphabetical characters
                        break
                    else:
                        raise ValueError("The input doesn't have alphabetical characters.")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop = False

            strngaloop = True
            while strngaloop:
                Address = str(input("Address: "))

                try:
                    if Address.isalpha():  # check if user input contains only alphabetical characters
                        break
                    else:
                        raise ValueError("The input doesn't contain alphabetical characters.")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    strngloop1 = False

            numbeloop = True
            while numbeloop:
                try:
                    contactnumber = int(input(
                        "contact_number: "))  # Prompt user to enter a contact number and convert the input to an integer
                except ValueError:
                    print("Enter a numeric value")  # Inform the user that they entered a non-numeric value
                else:
                    numbeloop = False  # Exit the loop if user input is a numeric value

            List = []  # Initialize an empty list to store the laptop purchases
            while loop:
                id = True  # Set id to True to enter the loop for validation of laptop id
                dict = read.myfunction()  # Get the dictionary of available laptops
                while id:
                    laptop_id = Operation.validation_lp_num(dict)  # Validate the entered laptop id
                    print(
                        f"Available stocks {dict[laptop_id][3]} only")  # Display the available stock of the selected laptop
                    if int(dict[laptop_id][3]) == 0:
                        Operation.loop(id)  # If the stock is 0, prompt the user to try again
                    else:
                        id = False  # Exit the loop if there is stock of the selected laptop
                quantity_of_laptop = Operation.quantity_validation(dict, laptop_id,
                                                                   user_ask)  # Validate the quantity of the selected laptop to be purchased
                dict = Operation.dictonary_update_sell(laptop_id, quantity_of_laptop,
                                                       List)  # Update the dictionary with the purchased quantity of the selected laptop
                Write.update(dict)  # Write the updated dictionary to the file
                loop_1 = True
                while loop_1:
                    ask_again = str(input(
                        "Do you want to buy again : "))  # Prompt the user to ask if they want to purchase more laptops
                    if ask_again == 'y':
                        loop_1 = False
                        loop = True  # If the user wants to buy more laptops, exit the inner loop and continue the outer loop
                    elif ask_again == 'n':
                        loop_1 = False
                        loop = False  # If the user doesn't want to buy more laptops, exit both the inner and outer loops
                    else:
                        print(
                            "Invalid value1press Y for Yes and N for NO1")  # Inform the user that they entered an invalid value

            bill_no = random.randint(0, 500)  # Generate a random bill number
            date = datetime.datetime.now().strftime("%d/%m/%Y")  # Get the current date
            time = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current time
            Write.bill(userName, Address, contactnumber, List, bill_no, date,
                       time)  # Generate the bill for the laptop purchases
            Write.bill_sell(userName, Address, contactnumber, List, bill_no, date,
                            time)  # Generate the sell bill for the laptop purchases
            print("\n")
            print("Thankyou for you  C0-opreation.")  # Display the message after the purchase is complete
        # ...

        elif user_ask == 2:

            # If user chooses option 2

            read.display()  # Display the available laptops

            print(
                "------------------------------------------------------------------------------------------------------------------")

            user_name = input("Name: ")  # Get user's name

            dict = read.myfunction()  # Retrieve the dictionary of available laptops

            list = []  # Initialize empty list for user's purchase history

            loop = True

            while loop == True:  # Loop until user is done purchasing

                laptop_id = int(input("Enter the laptop ID you want to buy :  "))  # Ask user to input laptop ID

                quantity_of_laptop = Operation.quantity_validation(dict, laptop_id,
                                                                   user_ask)  # Validate user's input for quantity

                dict = Operation.dictonary_update_purchase(laptop_id, quantity_of_laptop,
                                                           list)  # Update the dictionary after purchase

                Write.update(dict)  # Write the updated dictionary to file

                loop_1 = True

                while loop_1:  # Loop until user answers if they want to buy more

                    ask_again = str(input("Do you want to buy again : "))

                    # print("\n")

                    print("-----------------------------------------------------------------------")

                    if ask_again == 'y':  # If user wants to buy more

                        loop_1 = False

                        loop = True

                    elif ask_again == 'n':  # If user is done purchasing

                        loop_1 = False

                        loop = False

                    else:  # If user input is invalid

                        print("Invalid valuepress y for Yes anf n for No")

            bill_no = random.randint(0, 500)  # Generate random bill number

            date = datetime.datetime.now().strftime("%d/%m/%Y")  # Get current date

            time = datetime.datetime.now().strftime("%H:%M:%S")  # Get current time

            Write.biil_purchase(user_name, list, bill_no, date, time)  # Write purchase history to purchase file

            Write.bill_text_purchases(user_name, list, bill_no, date, time)  # Write purchase history to text file

            print("\n")

            print("Thank you for your co-opreation,Have a good Day")
            # ...

        elif user_ask == 3:
            # Code for Exit operation
            loop = False
            print("Exiting the program...")

User_option()
