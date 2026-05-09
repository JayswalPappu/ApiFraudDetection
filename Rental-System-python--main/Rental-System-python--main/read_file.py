# read_file.py

# Function to load lands data from 'land.txt' file
def load_lands():
    lands = []  # List to store lands information
    try:
        # Open the file in read mode
        with open('land.txt', 'r') as file:
            # Read each line and split into different fields
            for line in file:
                parts = line.split(',')
                # Add land data to the lands list as a dictionary
                lands.append({
                    'kitta': parts[0],             # Kitta number
                    'location': parts[1],          # Location of the land
                    'direction': parts[2],         # Direction of the land
                    'aana': int(parts[3]),         # Size in aana
                    'price': int(parts[4]),        # Price per aana
                    'status': parts[5].strip()     # Status of the land (Available/Rented)
                })
    except FileNotFoundError:
        # Handle case when the file doesn't exist
        print("Error: The file 'land.txt' does not exist. Please create it with valid data.")
    except Exception as e:
        # Catch any other exceptions
        print("An error occurred: " + str(e))
    return lands  # Return the list of lands

# Function to save lands data back to 'land.txt' file
def save_lands(lands):
    # Open the file in write mode
    with open('land.txt', 'w') as file:
        # Write each land's data as a comma-separated line
        for land in lands:
            file.write(
                land['kitta'] + ',' +         # Kitta number
                land['location'] + ',' +      # Location of the land
                land['direction'] + ',' +     # Direction of the land
                str(land['aana']) + ',' +     # Size in aana
                str(land['price']) + ',' +    # Price per aana
                land['status'] + '\n'         # Status of the land (Available/Rented)
            )
