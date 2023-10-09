# Function to separate digits of a number in a list
def separate_digits(number):
    return [int(digit) for digit in str(number)]

# Example usage
input_number = 10
result = separate_digits(input_number)
print(result)
