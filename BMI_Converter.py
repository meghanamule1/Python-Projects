feet = float(input("enter number in feet : "))
cm = feet * 30.48
print("cm as a height : ",cm)


height = float(input("enter the height in cm : "))
weight = float(input("enter the weight in kg  : "))

# Here we will be dividing the height by 100 to convert the centimetres into meters.

#BMI(Body Mass Index)  = kg / cm * cm

BMI = weight / (height/100)**2

print("You BMI is ",BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")