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
    
#summary 
if n >= 4:
    print(f"{name}, your plan is strong. you are aiming for {n} workouts each week.")
elif 1 <= n < 4:
    print(f"{name},your plan is good start.{n} workouts each week is realistic.")
else:
    print(f"{name},please choose a positive number of workouts.")


#water_check
water = int(input("how many glasses of water do you want to drink each day?"))
if water <= 4:
    print("you should improve your hydration")
else :
    print(f"{name} good job, that is a healthy hydration goal")


#sleep_goal
sleep = int(input("How many hours of sleep you want each night? "))
if sleep <  6:
    print("you need to improve your sleeping time")
else :
    print(f"good target {name} thats a optimal sleeping time ")


#final_summary
print(f"{name}!! you have set very good goals like {weekly_target} which are practical to achieve in age {age}")
print(f"your goals : \n Weekly workout : {n} workout sessions a week \n Hydration goal : {water} glasses per day \n sleep_goal : {sleep} hours per day")

                  