print("Welcome to the tip calculator")
#inputs to determine variables for amount of bill, number of people and how much tip %
bill_total = int(input("How much is the total bill?"))
group_size = int(input("How many people are in your group?"))
tip = int(input("How much percentage of tip would you like to leave? 10, 12, or 15?"))
#calculate bill per tip amount
if tip == 10:
    bill_total = bill_total * 1.1
elif tip == 12:
    bill_total = bill_total * 1.12
else:
    bill_total = bill_total * 1.15
#format number to 2 decimal places
final_bill = "{:.2f}".format(bill_total)
#calculate bill per person in group
bill_per_person = bill_total / group_size
amount_to_pay = round(bill_per_person, 2)
print(f'Your total bill is £{final_bill}, each person will need to pay £{amount_to_pay}')

