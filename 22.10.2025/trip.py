def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "charlotte" or city == "Charlotte":
        return 183
    elif city == "tampa" or city == "Tampa":
        return 220
    elif city == "pittsburgh" or city == "Pittsburgh":
        return 222
    elif city == "los angeles" or city == "Los Angeles":
        return 475
    else:
        return 0

def rental_car_cost(days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3:
        return days * 40 - 20
    else:
        return days * 40

def trip_cost(city, days, spending_money):
    return(rental_car_cost(days) +
           hotel_cost(days) + plane_ride_cost(city) + spending_money)

print("Cost of car rental:", rental_car_cost(6))

print("Cost of plane ride:", plane_ride_cost("Los Angeles"))

print("Cost of Hotel room:", hotel_cost(7))

print("Total trip cost:", trip_cost("Tampa", 6, 500))
