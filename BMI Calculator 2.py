print("--------------")
print("BMI CALCULATOR")
print("--------------")


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


Bmi = float(weight) / (float(height) ** 2)
total = round(Bmi)

if Bmi < 18.5:
    print(f"Your BMI is {total}, you are underweight")
elif Bmi < 25:
    print(f"Your BMI is  {total}, you have a normal weight")
elif Bmi < 30:
    print(f"Your BMI is {total}, you are slightly overweight")
elif Bmi < 35:
    print(f"Your BMI is {total}, you are obese")
else:
    print(f"Your BMI is {total}, You are clinically obese")



