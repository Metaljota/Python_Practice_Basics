print("--------------")
print("BMI CALCULATOR")
print("--------------")

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

Bmi = float(weight) / (float(height) ** 2)

result = int(Bmi)

#Using the "f" we can print out any data type with the string. 
print (f"Your BMI is: {result} ") 