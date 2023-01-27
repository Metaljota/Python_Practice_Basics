#INSTRUCTIONS

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("--------------")
print("TIP CALCULATOR")
print("--------------")

bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? Eg. 10, 12 or 15? ")
people = input("How many people to split the bill? ")

#this is the total tip to sum
tip_amount = (int(tip) / 100 ) * float(bill)

#this is the amount for each person to pay 
share = (float(bill) + tip_amount) / int(people)

#using round to use 2 decimal. ONE WAY
# print(f"Each person should pay: {round(share, 2)}")


#another WAY (for keeping the 2 decimal format)
share2 = "{:.2f}".format(share)

print(f"Each person should pay: {share2}")




