#greeting msg
name = input("what is your name? ")
goal = input("tell me your fitness goal")
print(f"Hello, {name}! Your goal is {goal}. Welcome to your fitness tracker.")

#more user data
age = int(input("enter your age"))
weekly_target = input("Enter your weekly fitness target")
print(f"for your age ({age}) this target - {weekly_target} is good")

#weekly workout
n = int(input("How many workouts do you want to do each week?"))
if n >= 4:
    print("strong plan")
elif 1 <= n < 4:
    print("good start")
elif n < 0:
    print("invalid entry")
else:
    print("enter a positive number")    
    
            