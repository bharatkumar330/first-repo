# Import the calculate_future_value function from the CarLoan file.
from CarLoan import calculate_future_value

# Create the new_car_loan dictionary.
new_car_loan = {
    "current_loan_value": 25000,
    "months_remaining": 12,
    "annual_interest_rate": 0.0315
    }

# Set the function call equal to a variable called car_value.
car_value = calculate_future_value(**new_car_loan)
# Pass the relevant information from the dictionary as parameters to the function call.

# Print the future value of the car to 2 decimal places.
print(car_value)
