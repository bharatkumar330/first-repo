# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_data = input("Enter your savings balance, interest rate, and maturity period (separated by spaces): ").split()
    savings_balance, savings_interest = map(float, savings_data[:-1])
    savings_maturity = int(savings_data[-1])

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated Savings Balance: {updated_savings_balance}")
    print(f"Interest Earned: {interest_earned}")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_data = input("Enter your CD balance, interest rate, and maturity period (separated by spaces): ").split()
    cd_balance, cd_interest = map(float, cd_data[:-1])
    cd_maturity = int(cd_data[-1])
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated CD Account Balance: {updated_cd_balance}")
    print(f"Interest Earned: {interest_earned}")
if __name__ == "__main__":
    # Call the main function.
    main()