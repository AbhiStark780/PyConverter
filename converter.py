"""
    PyConvertor : A CLI unit convertor
    It converts the units using a dictionary architecture
"""

# Dictionary for storing CONVERSION_RATES rates
CONVERSION_RATES = {
    "Length": {
        "km_to_miles":0.621371,
        "miles_to_km":1.60934
    },
    "Weight": {
        "kg_to_lbs":2.20462,
        "lbs_to_kg":0.453592
    }
}


def main():
    """
        Main Application Loop. 
        Handle user input, validation,
        and displays conversion results.
    """
    # Print the program name
    print("\nWelcome to PyConverter!")

    # List of all the categories available
    categories = list(CONVERSION_RATES.keys()) 

    while True:
        try:
            # Display all the available categories with index
            print("\n---- CATEGORY ----")
            for index, category in enumerate(categories, 1):
                print(f"{index}. {category}")

            # Prompt the user for the choice and take input from the user
            selected_index = int(input("Select a Category(num): "))  # whu minus 1? because we have stared the index with 1 to access the category from the list we minus 1

            # Raise a error if invalid category is choosen
            if selected_index < 1 or selected_index > len(categories):
                print("Error: Invalid Selection Number !")
                continue
            
            # Store the selected category
            selected_category = categories[selected_index - 1]

            # Prompt the user for the input and the amount
            source_unit = input("Convert From: ").lower()
            target_unit = input("Convert To: ").lower()
            amount = float(input("Amount: "))

            # Generate the conversion key
            conversion_key = f"{source_unit}_to_{target_unit}"

            # Extraxt the conversion unit from the dictionary[CONVERSION_RATES]
            factor = CONVERSION_RATES[selected_category][conversion_key]

            result = amount * factor

            print(f"{amount} {source_unit} is {result:.2f} {target_unit}")
        except ValueError:
            print("Error: Please enter a valid number for amount and category !")
            continue
        except KeyError:
            print(f"Error: Unsupported format {source_unit} to {target_unit} !")
            continue

        # prompt the user if he wants to convert another number
        again = input("Convert Again (y/n): ")
        if again.lower() != "y":
            return

if __name__ == "__main__":
    main()