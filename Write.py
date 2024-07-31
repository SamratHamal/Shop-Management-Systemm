import read
shipiing=None

def update(dict):
    # open the file in write mode
    open_file = open("abc.txt", "w")

    # iterate through the dictionary values
    for i in dict.values():
        # write each value to the file as a comma-separated string
        open_file.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]))
        # add a newline character at the end of each line
        open_file.write("\n")

    # close the file
    open_file.close()


def bill(name, address, contact_num, list, bill_no, date, time):
    # use the global keyword to make 'shiping' a global variable
    global shipiing

    # prompt the user for shipping preference

    ship = True
    while ship:
        shipiing = input("Do you want to ship the prduct ?: (y/n)\n")
        if shipiing.lower() == "y":
            # If the customer wants shipping, set 'ship_cost' to 250
            ship = False
            ship_cost = 250
        elif shipiing.lower() == "n":
            # If the customer doesn't want shipping, set 'ship_1' to False and skip shipping cost
            ship = False
        else:
            print("Invalid! Please enter y for  yes or n for  no.")
    # create a flag to loop until the user inputs a valid value for shipping preference

    # call the 'header' function from the 'read' module
    read.header()

    # print the bill details
    print(f"\t\t\t\t\tBill no: {bill_no}")
    print(f"Date: {date}\t\t\t\t\t Time: {time}")
    print(f"Name:  {name}")
    print(f"Address: {address}")
    print(f"Number: {contact_num}")
    t_total = 0

    # iterate through the list of items
    for i in range(len(list)):
        c_name = list[i][1].replace(" ", "")
        # print the laptop name and company name
        print(f"Laptop Name: {list[i][0]}\t\t\t\tCompany: {c_name}")
        # get the price of the item and print the price and quantity
        price1 = list[i][2].replace(" ", "")
        print(f"Price: {price1}\t\t\t Quantity: {list[i][4]}")
        # calculate and print the total price for the item
        print(f"Total price: {list[i][3]}")
        # add the total price of the item to the total bill amount
        t_total = t_total + int(list[i][3])
        print(f"\n")

    # calculate and print the total bill amount
    if shipiing == "y":
        print(f"Shipping cost: {250}")
        print(f"Total: {t_total}")
        print(f"Grand total: {t_total + 250}")
    else:
        print(f"Total: {t_total}")


# Define a function to create and write to a new file for a sales bill
def bill_sell(name, address, contact_num, list, bill_no, date, time):
    # Open a new file with the bill number as the filename
    global shipiing
    file = open(f"{bill_no}.txt", "w")

    # Write the bill information to the file
    file.write(f"/t/t/tBill no: {bill_no}\n")
    file.write(f"Date: {date}\t\t\t\t\t Time: {time}\n")
    file.write(f"Name:  {name}\n")
    file.write(f"Address: {address}\n")
    file.write(f"Number: {contact_num}\n")

    # Calculate the total cost of the items purchased
    t_total = 0
    for i in range(len(list)):
        c_name = list[i][1].replace(" ", "")
        file.write(f"Laptop Name: {list[i][0]}\t\t\t\tCompany Name: {c_name}\n")
        price1 = list[i][2].replace(" ", "")
        file.write(f"Price: {price1}\t\t\t\t\t Quantity: {list[i][4]}\n")
        file.write(f"Total price: {list[i][3]}\n")
        t_total = t_total + int(list[i][3])
        file.write(f"\n")

    # If shipping is requested, add the shipping cost to the bill total
    if shipiing == "y":
        file.write(f"Shipping cost: {250}\n")
        file.write(f"Total: {t_total}\n")
        file.write(f"Grand total: {t_total + 250}\n")
    else:
        file.write(f"Total: {t_total}\n")


# Define a function to print a purchase bill to the console
def biil_purchase(name, list, bill_no, date, time):
    # Print the bill information to the console
    print(f"\t\t\t\t\tBill no: {bill_no}")
    print(f"Date: {date}\t\t\t\t\t Time: {time}")
    print("-------------------------------------------------------------------------")
    print(f"Name:  {name}")

    # Calculate the total cost of the items purchased
    t_total = 0
    for i in range(len(list)):
        c_name = list[i][1].replace(" ", "")
        print(f"Laptop Name: {list[i][0]}")
        print(f"Company Name: {c_name}")  # TODO: Write to file instead of printing
        price1 = list[i][2].replace(" ", "")
        print(f"Price: {price1}")
        print(f"Quantity: {list[i][4]}")
        print(f"Total price: {list[i][3]}")
        t_total = t_total + int(list[i][3])
        print(f"\n")

    # Calculate and print the VAT and grand total of the purchase
    print(f"VAT amount: {0.13 * t_total}")
    print(f"Grand Total :{(0.13 * t_total) + t_total}")


# Define a function to create a text file for a purchase bill with given parameters
def bill_text_purchases(name, list, bill_no, date, time):
    # Open a text file with the given bill number in write mode
    file = open(f"{bill_no}.txt", "w")

    # Write bill details to the file
    file.write(f"\\t\t\t\tBill no: {bill_no}\n")  # Write the bill number
    file.write(f"date: {date}\t\t\t\t\t Time: {time}\n")  # Write the date and time of purchase
    file.write(f"name:  {name}\n")  # Write the name of the customer
    t_total = 0  # Initialize total price variable

 # Loop through the list of items purchased and write their details to the file
    for i in range(len(list)):
        c_name = list[i][1].replace(" ", "")  # Get the company name and remove any spaces
        file.write(f"Laptop Name: {list[i][0]}\t\t\t\tCompany Name: {c_name}\n")  # Write laptop name and company name
        price1 = list[i][2].replace(" ", "")  # Get the price and remove any spaces
        file.write(f"Price: {price1}\t\t\t\t\t \nQuantity: {list[i][4]}\n")  # Write the price and quantity
        file.write(f"Total price: {list[i][3]}\n")  # Write the total price for the item
        t_total = t_total + int(list[i][3])  # Add the item price to the total price
        file.write(f"\n")  # Write a blank line for formatting

    file.write(f"vat amount: {0.13 * t_total}\n")  # Calculate and write the VAT amount
    file.write(f"Grand Total = {(0.13 * t_total) + t_total}\n")  # Calculate and write the grand total (including VAT)
