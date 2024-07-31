# Function to display the header part of GUI
def header():
    '''this functon shows the header part of gui'''
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t \t \t \t  Kathamandu Electronic Store")  # Display store name
    print("\n")
    print("\t \t \t \t \t \t \t \t  Putalisadak , kathmandu  | 98089712345")  # Display store location and contact number
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

# Function to read data from a file and store in a dictionary
def myfunction():
    """function to show the values present in the dictonary"""
    dictonary = {}  # Create an empty dictionary
    file = open("abc.txt", "r")  # Open the file in read mode
    laptopid = 1  # Initialize laptop ID to 1
    for data in file:  # Read data from the file line by line
        data = data.replace("\n", "")  # Remove newline character
        dictonary.update({laptopid : data.split(",")})  # Split the line using comma as delimiter and add it as a value to the dictionary with laptop ID as key
        laptopid += 1  # Increment laptop ID for the next iteration
    file.close()  # Close the file
    #print(dictonary)  # Optional: Print the dictionary for debugging purposes
    return dictonary  # Return the dictionary

# Function to display laptop details in a table format
def display():

    with open("abc.txt", "r") as f:  # Open the file in read mode using 'with' statement for better file handling
        print("-" * 150)  # Print a horizontal line separator
        print("{:<10}{:<30}{:<30}{:<20}{:<15}{:<25}{:<35}".format("S.N", "Name", "Brand", "Price", "Quantity", "Processor", "Graphics Card"))  # Print header row with column names
        print("-" * 150)  # Print a horizontal line separator
        for i, line in enumerate(f, start=1):  # Read data from the file line by line and enumerate the lines starting from 1
            fields = line.strip().split(",")  # Split the line using comma as delimiter and store the resulting list in 'fields'
            print("{:<10}{:<30}{:<30}{:<20}{:<15}{:<25}{:<35}".format(i, *fields))  # Format and print the line using the values in 'fields'
    return
