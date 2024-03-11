def get_city():
    #Prompt the user to input a city, ensuring it's one of the predefined destinations.
    cities = ["New York", "London", "Venice", "Paris"]
    while True:
        city = input("Enter the city you want to fly to (New York, London, Venice, Paris): ")
        if city in cities:
            return city
        else:
            print("Please choose from the listed destinations.")

def get_positive_integer(prompt):
    #Prompt the user to input a positive integer, ensuring the input is valid.
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")

def hotel_cost(num_nights):
    #Calculate the cost of the hotel stay.
    return 140 * num_nights

def plane_cost(city_flight):
    #Calculate the cost of the plane ticket based on the destination.
    flight_costs = {
        "New York": 500,
        "London": 450,
        "Venice": 250,
        "Paris": 300
    }
    return flight_costs.get(city_flight, 0)

def car_rental(rental_days):
    #Calculate the cost of the car rental.
    return 40 * rental_days

def holiday_cost(hotel_cost, plane_cost, car_rental):
    #Calculate the total cost of the holiday.
    return hotel_cost + plane_cost + car_rental

# Main program
city_flight = get_city()
num_nights = get_positive_integer("Enter the number of nights you want to stay: ")
rental_days = get_positive_integer("Enter the number of days you want to rent a car: ")

total_cost = holiday_cost(
    hotel_cost(num_nights),
    plane_cost(city_flight),
    car_rental(rental_days)
)

print(f"The total cost of your holiday is: {total_cost}")
