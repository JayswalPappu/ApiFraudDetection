# operations.py

# Import necessary modules
import write_file
import read_file

# Validation functions to ensure data is valid
def is_name_valid(name):
    return name.isalpha()  # Check if the name contains only letters

def is_phone_valid(phone):
    return len(str(phone)) == 10  # Check if the phone number has 10 digits

def is_numeric(value):
    return value.isdigit()  # Check if the value is numeric

def is_positive(value):
    return value > 0  # Check if the value is positive

def is_aana_valid(aana, required_aana):
    return aana == required_aana  # Check if the requested aana matches the required aana

def has_enough_months(current, rented):
    return current >= rented  # Check if there are enough months

def validate_aana(aana, required_aana):
    return aana == required_aana  # Ensure the requested aana matches the required aana

def validate_months(current, rented):
    return current >= rented  # Ensure enough months have passed

# Function to get validated input from the user
def get_input(msg, data_type, validation_fn=None, validation_args=None, error_msg="Invalid input."):
    while True:
        value = input(msg)  # Prompt the user for input
        try:
            val = data_type(value)  # Convert input to the specified data type
            if validation_fn:  # If a validation function is provided
                if validation_args:
                    if not validation_fn(val, *validation_args):
                        raise ValueError()  # Raise an error if validation fails
                else:
                    if not validation_fn(val):
                        raise ValueError()  # Raise an error if validation fails
            return val  # Return the validated value
        except ValueError:
            print(error_msg)  # Print an error message if validation fails

# Function to display all available lands
def show_lands(lands):
    for land in lands:
        print('Kitta = ' + land['kitta'] + '\t\t located in = ' + land['location'] +
              ' \t\t facing = ' + land['direction'] + '\t\t with = ' +
              str(land['aana']) + ',aana, \t\t priced = NRP.' +
              str(land['price']) + ',\t\t Status = ' + land['status'])

# Function to rent land
def rent_land(lands, direct_process=False):
    while True:
        show_lands(lands)  # Display all lands

        # Get user input for renting land
        name = get_input('\nEnter your name: ', str, is_name_valid, None, 'Please enter only alphabetic characters.')
        phone = get_input('Enter your phone number (numerical values only): ', int, is_phone_valid, None, 'Phone number must have 10 digits.')
        kitta = get_input('Enter the kitta number you want to rent: ', str, is_numeric, None, 'Please enter a valid numerical kitta number.')

        found = False  # Track if the kitta is found
        for land in lands:
            if land['kitta'] == kitta:
                found = True
                if land['status'] == 'Available':
                    # Get user input for aana and months
                    aana = get_input('\nEnter the number of aana you want to rent: ', int, validate_aana, [land['aana']], 'Invalid aana number. You have to take all available aana: ' + str(land['aana']))
                    months = get_input('Enter the duration of the rent (in months): ', int, is_positive, None, 'Please enter a valid positive number of months.')

                    # Calculate total cost
                    total = land['price'] * months

                    # Write the rental invoice and update land status
                    write_file.rent_invoice(name, str(phone), kitta, aana, months, total)
                    land['status'] = 'Rented'
                    read_file.save_lands(lands)
                    break
        if not found:
            print('Kitta number is not available.')

        # Ask if the user wants to rent more land
        more = input('\nDo you want to rent more land? Yes/No: ').lower()
        if more == 'no':
            if direct_process:
                break
            else:
                return

# Function to return rented land
def return_land(lands, direct_process=False):
    while True:
        show_lands(lands)  # Display all lands

        # Get user input for returning land
        name = get_input('\nEnter your name: ', str, is_name_valid, None, 'Please enter only alphabetic characters.')
        kitta = get_input('Enter the kitta number you are returning: ', str, is_numeric, None, 'Please enter a valid numerical kitta number.')

        found = False  # Track if the kitta is found
        for land in lands:
            if land['kitta'] == kitta:
                found = True
                if land['status'] == 'Rented':
                    # Get user input for rented and current months
                    rented_months = get_input('Enter how many months you rented the land: ', int, is_positive, None, 'Please enter a valid positive number of months.')
                    current_months = get_input('Enter how many months have passed since you rented the land: ', int, validate_months, [rented_months], 'Please enter a valid number of months passed.')

                    # Calculate total, extra amount, and fine
                    total = land['price'] * rented_months
                    extra_months = max(0, current_months - rented_months)
                    extra_amount = extra_months * land['price']
                    fine = extra_amount * 0.10  # 10% fine
                    total_due = total + fine + extra_amount

                    # Write the return invoice and update land status
                    write_file.return_invoice(name, kitta, rented_months, total, extra_months, fine, total_due)

                    land['status'] = 'Available'
                    read_file.save_lands(lands)
                    break
                else:
                    print('This kitta is currently not rented. Check the kitta number or its status.')
        if not found:
            print('Kitta number is not available.')

        # Ask if the user wants to return more land
        more = input('\nDo you want to return more land? Yes/No: ').lower()
        if more == 'no':
            if direct_process:
                break
            else:
                return
