# write_file.py

# Function to save the invoice text to a file
def save_invoice(text, filename):
    # Open the file in append mode
    with open(filename, 'a') as file:
        # Write the invoice text followed by two new lines
        file.write(text + '\n\n')

# Function to create and display a rent invoice
def rent_invoice(name, phone, kitta, aana, months, total):
    # Prepare the invoice text
    text = (
        "Invoice:\n"
        "Rent by " + name + ",\n"
        "Phone: " + phone + ",\n"
        "Kitta: " + kitta + ",\n"
        "Aana: " + str(aana) + ",\n"
        "Duration: " + str(months) + " months,\n"
        "Total Amount: " + str(total)
    )
    # Display the invoice in the console
    print("*" * 50)
    print(text)
    print("*" * 50)
    # Create a filename for the invoice based on the user's name
    filename = name.replace(" ", "_").lower() + '_rent_invoice.txt'
    # Save the invoice text to the file
    save_invoice(text, filename)

# Function to create and display a return invoice
def return_invoice(name, kitta, rented_months, total, extra_months, fine, total_due):
    # Prepare the invoice text
    text = (
        "Invoice:\n"
        "Return by " + name + ",\n"
        "Kitta: " + kitta + ",\n"
        "Rented for: " + str(rented_months) + " months,\n"
        "Original Total: " + str(total) + ",\n"
        "Extra Months: " + str(extra_months) + ",\n"
        "Fine: " + str(fine) + ",\n"
        "Total Amount Due: " + str(total_due)
    )
    # Display the invoice in the console
    print("*" * 50)
    print(text)
    print("*" * 50)
    # Create a filename for the invoice based on the user's name
    filename = name.replace(" ", "_").lower() + '_return_invoice.txt'
    # Save the invoice text to the file
    save_invoice(text, filename)
