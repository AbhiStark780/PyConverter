# Dictionary for storing CONVERSION rates
CONVERSION = {
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
    # Print the program name
    print("Welcome to PyConverter!")

    while True:
        # Give the user option to select
        print("1.Length")
        print("2.Weight")

        # Prompt the user for the choice and take input from the user
        try:
            choice = int(input("Select a Category: "))
            Value_From = input("Convert from: ")
            Value_To = input("Convert To: ")
            amount = float(input("Amount: "))
        except ValueError:
            print("Enter a Valid Amount !")
            continue

        try:
            if choice == 1:
                result = amount*CONVERSION["Length"][f"{Value_From.lower()}_to_{Value_To.lower()}"]
                print(f"Result: {amount} {Value_From} is {result:.2f} {Value_To}")
            elif choice == 2:
                result = amount*CONVERSION["Weight"][f"{Value_From.lower()}_to_{Value_To.lower()}"]
                print(f"Result: {amount} {Value_From} is {result:.2f} {Value_To}")
        except KeyError:
            print("Unsupported Units!")
            continue

        # prompt the user if he wants to convert another number
        again = input("Convert Again (y/n): ")
        if again.lower() != "y":
            return

main()