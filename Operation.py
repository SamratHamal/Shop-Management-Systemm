import read

def dictionary_update(pc_id, laptop_count, lst):
    file = read.myfunction()
    if pc_id not in file:
        raise ValueError("Invalid laptop ID")
    
    quantity = int(file[pc_id][3])
    if laptop_count > quantity:
        raise ValueError("Not enough stock available")

    file[pc_id][3] = str(quantity - laptop_count)
    price = laptop_count * int(file[pc_id][2].replace("$", ""))
    lst.append([file[pc_id][0], file[pc_id][1], file[pc_id][2], price, laptop_count])
    
    return file


def dictionary_update_purchase(pc_id, laptop_quantity, lst):
    file = read.myfunction()
    for a in file.keys():
        if pc_id == a:
            quantity = int(file[pc_id][3])
            file[pc_id][3] = str(quantity + laptop_quantity)
            price = laptop_quantity * int(file[pc_id][2].replace("$", ""))
            lst.append([file[pc_id][0], file[pc_id][1], file[pc_id][2], price, laptop_quantity])
    return file


def validation_lp_num(dictionary):
    validation_loop = True
    v_values = list(dictionary.keys())
    pause = v_values[-1]
    while validation_loop:
        try:
            laptop_id = int(input("Enter the laptop ID: "))
        except ValueError:
            print("Enter a valid value")
        else:
            if laptop_id <= 0:
                print("Enter a valid ID")
            elif 0 <= laptop_id <= pause:
                validation_loop = False
            else:
                print("Invalid Input")
    return laptop_id


def quantity_validation(dict, laptop_id, input_from_user):
    if laptop_id not in dict:
        raise ValueError("Invalid laptop ID")

    quantity_available = int(dict[laptop_id][3])

    valid_loop = True
    while valid_loop:
        try:
            quantity_of_laptop = int(input("Enter the quantity of laptops: "))

            if quantity_of_laptop < 0:
                raise ValueError("Negative values are not allowed")

            if input_from_user == 1 and quantity_of_laptop > quantity_available:
                raise ValueError("Not enough stock available")

        except ValueError as err:
            print("Invalid input:", err)
        else:
            valid_loop = False

    return quantity_of_laptop


def loop():
    loop_1 = True
    while loop_1:
        ask_again = input("Do you want to buy again? (Y/N): ").lower()
        if ask_again == 'y':
            loop_1 = False
            loop_val = True
        elif ask_again == 'n':
            loop_1 = False
            loop_val = False
        else:
            print("Invalid command. Please select Y for Yes and N for No.")
    return loop_val
