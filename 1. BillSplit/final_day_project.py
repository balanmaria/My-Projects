print("Welcome to the tip calculator.")
bill=input("What was the total bill? $")
percentage=input("What percentage tip would you like to give? 10, 12, or 15?\n")
people=input("How many people to split the bill?\n")
int_bill=float(bill)
int_percentage=int(percentage)
tips=(int_percentage/100)*int_bill
final_bill= int_bill + tips #final_bill=int_bill * (int_percentage/100)
int_people=int(people)
should_pay="{:.2f}".format(final_bill/int_people)
print(f"Each person should pay: ${should_pay}")