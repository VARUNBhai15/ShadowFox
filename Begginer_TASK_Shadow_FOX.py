#Variables Task One

pi=22/7
print("the value of pi is :",pi,"\n")


P = 2700
R = 3
T = 2

SI= P * R * T/100
print("The Simple Intrest is:",SI,"\n")


# Justice League List Task

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Original List:", justice_league)

# Number of members
print("Number of members:", len(justice_league))

# Add Batgirl & Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding members:", justice_league)

# Move Wonder Woman to beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("New Leader:", justice_league)

#if Condition Tasks Three

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")

print("\n")

#Task Four For Loop


import random

rolls = 20
count_6 = 0
count_1 = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print("Roll:", roll)

    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1

print("Total 6s:", count_6)
print("Total 1s:", count_1)

#Task Five Class
class Student:
    pass

s1 = Student()
s1.name = "Varun"
s1.age = 20

print("Name:",s1.name)
print("Age:",s1.age)
