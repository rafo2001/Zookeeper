# get inputs
days = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_night = int(input())
# do the maths
total_cost = (flight_cost * 2) + (days * food_cost) + (hotel_night * (days - 1))
# print results
print(total_cost)