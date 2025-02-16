# Write code below 💖

credits=int(input("Enter the number of credits "))
height= int(input("Enter your height "))

if (credits>=10) and (height>=137):
    print('Enjoy the ride!')
elif (credits>=10) and (height<137):
    print("You are not tall enough to ride.")
elif (credits<10) and (height>=137):
    print("You don't have enough credits.")
else:
    print("You don't have met either requirement")

