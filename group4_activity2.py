"Group 4 Natnael Argaw, Shaikha Alghubash, Sayyed Abedin"

# Constants for conversion rates
CONVERSION_RATE_OF_AED_TO_EUR = 0.27
CONVERSION_RATE_OF_AED_TO_GBP = 0.23
CONVERSION_RATE_OF_AED_TO_USD = 0.27
CONVERSION_RATE_OF_EUR_TO_AED = 3.7
CONVERSION_RATE_OF_GBP_TO_AED = 4.35
CONVERSION_RATE_OF_USD_TO_AED = 3.67

# Function to convert AED to Euro
def aed_to_eur(money):
    """Convert AED to Euro."""
    return money * CONVERSION_RATE_OF_AED_TO_EUR

# Function to convert AED to British Pound
def aed_to_britishPound(money):
    """Convert AED to British Pound."""
    return money * CONVERSION_RATE_OF_AED_TO_GBP

# Function to convert AED to US Dollar
def aed_to_dollar(money):
    """Convert AED to US Dollar."""
    return money * CONVERSION_RATE_OF_AED_TO_USD

# Function to convert US Dollar to AED
def dollar_to_aed(money):
    """Convert US Dollar to AED."""
    return money * CONVERSION_RATE_OF_USD_TO_AED

# Function to convert British Pound to AED
def britishPound_to_aed(money):
    """Convert British Pound to AED."""
    return money * CONVERSION_RATE_OF_GBP_TO_AED

# Function to convert Euro to AED
def eur_to_aed(money):
    """Convert Euro to AED."""
    return money * CONVERSION_RATE_OF_EUR_TO_AED

# Helper function to get a valid positive float input
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The amount must be greater than 0. Please enter a positive value.")
            return value
        except ValueError:
            print("Please enter a numeric value")

# Helper function to get a valid choice input
def get_valid_choice(prompt, choices):
    while True:
        choice = input(prompt)
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please enter a valid option.")

# Main function for user interaction
def main():
    while True:
        print("\nWelcome to Currency Converter")
        print("---------------------------------")
        print("Select the conversion direction:")
        print("1. AED to other currencies")
        print("2. Other currencies to AED")
        print("3. Exit")
        
        choice = get_valid_choice("Enter your choice (1/2/3): ", ["1", "2", "3"])

        if choice == "1":
            amount = get_positive_float("Enter the amount in AED you want to convert: ")
            print("1. AED to Euro (EUR)")
            print("2. AED to British Pound (GBP)")
            print("3. AED to US Dollar (USD)")
            sub_choice = get_valid_choice("Enter the Sub choice of currency (1/2/3): ", ["1", "2", "3"])

            if sub_choice == "1":
                print(f"{amount} AED is equal to {aed_to_eur(amount)} EUR")
            elif sub_choice == "2":
                print(f"{amount} AED is equal to {aed_to_britishPound(amount)} GBP")
            elif sub_choice == "3":
                print(f"{amount} AED is equal to {aed_to_dollar(amount)} USD")

        elif choice == "2":
            amount = get_positive_float("Enter the amount you want to convert to AED: ")
            print("1. Euro (EUR) to AED")
            print("2. British Pound (GBP) to AED")
            print("3. US Dollar (USD) to AED")
            sub_choice = get_valid_choice("Enter the Sub choice of currency (1/2/3): ", ["1", "2", "3"])

            if sub_choice == "1":
                print(f"{amount} EUR is equal to {eur_to_aed(amount)}")
            elif sub_choice == "2":
                print(f"{amount} GBP is equal to {britishPound_to_aed(amount)}")
            elif sub_choice =="3":
                print(f"{amount} USD is equal to {dollar_to_aed(amount)}")



if __name__ == "__main__":
    main()
