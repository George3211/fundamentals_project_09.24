cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "rental_price": 30, "availability": True},
    {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "availability": True},
    {"id": 3, "brand": "Ford", "model": "Focus", "rental_price": 25, "availability": True},
    {"id": 4, "brand": "Chevrolet", "model": "Malibu", "rental_price": 28, "availability": True},
    {"id": 5, "brand": "Nissan", "model": "Altima", "rental_price": 32, "availability": True},
    {"id": 6, "brand": "Hyundai", "model": "Elantra", "rental_price": 27, "availability": True},
    {"id": 7, "brand": "Volkswagen", "model": "Passat", "rental_price": 33, "availability": True},
    {"id": 8, "brand": "Kia", "model": "Optima", "rental_price": 29, "availability": True},
    {"id": 9, "brand": "Subaru", "model": "Impreza", "rental_price": 26, "availability": True},
    {"id": 10, "brand": "Mazda", "model": "Mazda3", "rental_price": 31, "availability": True},
    {"id": 11, "brand": "BMW", "model": "3 Series", "rental_price": 50, "availability": True},
    {"id": 12, "brand": "Mercedes-Benz", "model": "C-Class", "rental_price": 55, "availability": True},
    {"id": 13, "brand": "Audi", "model": "A4", "rental_price": 52, "availability": True},
    {"id": 14, "brand": "Lexus", "model": "IS", "rental_price": 48, "availability": True},
    {"id": 15, "brand": "Acura", "model": "TLX", "rental_price": 45, "availability": True},
    {"id": 16, "brand": "Infiniti", "model": "Q50", "rental_price": 47, "availability": True},
    {"id": 17, "brand": "Tesla", "model": "Model 3", "rental_price": 60, "availability": True},
    {"id": 18, "brand": "Volvo", "model": "S60", "rental_price": 53, "availability": True},
    {"id": 19, "brand": "Jaguar", "model": "XE", "rental_price": 58, "availability": True},
    {"id": 20, "brand": "Alfa Romeo", "model": "Giulia", "rental_price": 56, "availability": True},
    {"id": 21, "brand": "Cadillac", "model": "ATS", "rental_price": 54, "availability": True},
    {"id": 22, "brand": "Genesis", "model": "G70", "rental_price": 49, "availability": True},
    {"id": 23, "brand": "Lincoln", "model": "MKZ", "rental_price": 51, "availability": True},
    {"id": 24, "brand": "BMW", "model": "5 Series", "rental_price": 70, "availability": True},
    {"id": 25, "brand": "BMW", "model": "X5", "rental_price": 80, "availability": True},
    {"id": 26, "brand": "Audi", "model": "Q7", "rental_price": 75, "availability": True},
    {"id": 27, "brand": "Audi", "model": "A6", "rental_price": 65, "availability": True},
    {"id": 28, "brand": "Mercedes-Benz", "model": "E-Class", "rental_price": 68, "availability": True},
    {"id": 29, "brand": "Mercedes-Benz", "model": "GLC", "rental_price": 72, "availability": True},
    {"id": 30, "brand": "Lamborghini", "model": "Huracan", "rental_price": 200, "availability": True},
    {"id": 31, "brand": "Lamborghini", "model": "Aventador", "rental_price": 300, "availability": True},
    {"id": 32, "brand": "Lamborghini", "model": "Urus", "rental_price": 250, "availability": True},
    {"id": 33, "brand": "BMW", "model": "M3", "rental_price": 90, "availability": True},
    {"id": 34, "brand": "Toyota", "model": "RAV4", "rental_price": 40, "availability": True},
    {"id": 35, "brand": "Honda", "model": "CR-V", "rental_price": 42, "availability": True},
    {"id": 36, "brand": "Ford", "model": "Escape", "rental_price": 38, "availability": True},
    {"id": 37, "brand": "Chevrolet", "model": "Equinox", "rental_price": 37, "availability": True},
    {"id": 38, "brand": "Nissan", "model": "Rogue", "rental_price": 39, "availability": True},
    {"id": 39, "brand": "Hyundai", "model": "Tucson", "rental_price": 36, "availability": True},
    {"id": 40, "brand": "Volkswagen", "model": "Tiguan", "rental_price": 41, "availability": True},
    {"id": 41, "brand": "Kia", "model": "Sorento", "rental_price": 43, "availability": True},
    {"id": 42, "brand": "Subaru", "model": "Forester", "rental_price": 44, "availability": True},
    {"id": 43, "brand": "Mazda", "model": "CX-5", "rental_price": 45, "availability": True},
    {"id": 44, "brand": "BMW", "model": "X3", "rental_price": 85, "availability": True},
    {"id": 45, "brand": "Audi", "model": "Q5", "rental_price": 78, "availability": True},
    {"id": 46, "brand": "Mercedes-Benz", "model": "GLA", "rental_price": 70, "availability": True},
    {"id": 47, "brand": "Lamborghini", "model": "Urus", "rental_price": 250, "availability": True},
    {"id": 48, "brand": "Jeep", "model": "Grand Cherokee", "rental_price": 60, "availability": True},
    {"id": 49, "brand": "Land Rover", "model": "Range Rover", "rental_price": 150, "availability": True},
    {"id": 50, "brand": "Porsche", "model": "Cayenne", "rental_price": 140, "availability": True},
    {"id": 51, "brand": "Volvo", "model": "XC90", "rental_price": 130, "availability": True},
    {"id": 52, "brand": "Jaguar", "model": "F-Pace", "rental_price": 120, "availability": True},
    {"id": 53, "brand": "Alfa Romeo", "model": "Stelvio", "rental_price": 110, "availability": True},
    {"id": 54, "brand": "BMW", "model": "3 Series", "rental_price": 50, "availability": True},
    {"id": 55, "brand": "Audi", "model": "A4", "rental_price": 52, "availability": True},
    {"id": 56, "brand": "Mercedes-Benz", "model": "C-Class", "rental_price": 55, "availability": True,},
    {"id": 57, "brand": "BMW", "model": "5 Series", "rental_price": 70, "availability": True},
    {"id": 58, "brand": "Audi", "model": "A6", "rental_price": 65, "availability": True}
]

# Hiring status tracking dictionary
rental_status = {}


# Car rental function


def rent_car(car_id, user):
    for car in cars:
        if car["id"] == car_id and car["availability"]:
            car["availability"] = False
            rental_status[user] = {"car_id": car_id, "rental_price": car["rental_price"], "rental_duration": 0}
            print(f"Car {car['brand']} {car['model']} rented successfully!")
            return
    print("Car not available or invalid car ID.")


# Car return function


def return_car(user, rental_duration):
    if user in rental_status:
        car_id = rental_status[user]["car_id"]
        rental_price = rental_status[user]["rental_price"]
        total_cost = rental_price * rental_duration
        for car in cars:
            if car["id"] == car_id:
                car["availability"] = True
                break
        del rental_status[user]
        print(f"Car returned successfully! Total cost: ${total_cost}")
    else:
        print("No car rented by this user.")


# Function to display available cars


def view_available_cars():
    print("Available cars:")
    for car in cars:
        if car["availability"]:
            print(f'ID: {car["id"]}, Brand: {car["brand"]}, Model: {car["model"]}, \n'
                  f' Rental Price: ${car["rental_price"]} per day')


# view_available_cars()


def returning_car():
    #  function to return the car
    user_name = input("\nPlease, enter your names: ")
    # Prompt the user to enter his names.
    # Prompt the user to enter duration of the rent.
    duration_of_rent = int(input("Please, enter duration of the rent. Keep in mind, that the price is per day.\n"
                                 "If the day has started, the whole day is considered: "))

    if user_name in rental_status:  # Check if the user is in dictionary for rentals.
        return_car(user_name, duration_of_rent)  # calling function to return the car


def renting_car():  # function to rent the car
    while True:  # Loop that let user to input id again if chosen one is not available
        choice = int(input("\nChoose id of car you want to rent: "))
        for car in cars:
            # Check if chosen car is available, if it is, prompt user to input names, if not, prompt you for new input
            if car["id"] == choice and car["availability"]:
                name_user = input("\nPlease, enter your names. ")
                return rent_car(choice, name_user)  # calling function to rent the car
        print("Car not available or invalid car ID.\nPlease, try again.")


def display_cars():  # function to display available cars
    print("\nAvailable Cars:")
    view_available_cars()  # calling function to display available cars


def main_menu():
    """Display the main menu."""
    print("\nWelcome to RentACar")
    print("1. View Car")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    return int(input("Please choose an option (1-4): "))


def main():
    """Main function to run the platform."""
    while True:  # validation to ensure the user enters valid options
        choice = main_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            # calling function to display available cars
            display_cars()

        elif choice == 2:
            # Prompt the user to choose id of car and insert his names. Checking if the chosen car is available.
            # If available calling function to rent the car.
            renting_car()

        elif choice == 3:
            # Prompt the user to enter his names and duration of the rent.
            returning_car()

        elif choice == 4:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            # if the user enter invalid option, receive error message and return for new input
            print("Invalid choice. Please try again.")


main()
