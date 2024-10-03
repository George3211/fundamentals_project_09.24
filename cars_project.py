# Списък с коли, всяка кола е представена като речник
cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "rental_price": 30, "availability": True},
    {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "availability": True},
    {"id": 3, "brand": "Ford", "model": "Focus", "rental_price": 25, "availability": True}
]

# Речник за проследяване на статуса на наемане
rental_status = {}


# Функция за наемане на кола
def rent_car(car_id, user):
    for car in cars:
        if car["id"] == car_id and car["availability"]:
            car["availability"] = False
            rental_status[user] = {"car_id": car_id, "rental_price": car["rental_price"], "rental_duration": 0}
            print(f"Car {car['brand']} {car['model']} rented successfully!")
            return
    print("Car not available or invalid car ID.")


# Функция за връщане на кола
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


# Функция за показване на наличните коли
def view_available_cars():
    print("Available cars:")
    for car in cars:
        if car["availability"]:
            print(
                f"ID: {car['id']}, Brand: {car['brand']}, Model: {car['model']}, Rental Price: ${car['rental_price']} per day")


view_available_cars()
