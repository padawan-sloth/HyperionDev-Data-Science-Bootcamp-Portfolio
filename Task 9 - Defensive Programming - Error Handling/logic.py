# A program with a logical error

def check_temperature(temperature):
    # The function is intended to check if the temperature is in a comfortable range
    # Comfortable range is between 18 to 24 degrees Celsius
    
    # Logical Error: The conditions are incorrectly set, creating a logic that doesn't match the intention
    if temperature < 18:
        return "Too cold!"
    elif temperature > 24:
        return "Too hot!"
    else:
        # The logical error is here: it should say "Just right!" but it mistakenly says "Still not comfortable!"
        return "Still not comfortable!"

# Test the function with a temperature within the comfortable range
test_temperature = 22
comfort_check = check_temperature(test_temperature)
print(comfort_check)
