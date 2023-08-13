#Total Bill
bill_total = 214
#Disscount Amount
discount1 = 10
discount2 = 20
#Matching the condition and applying discount
if bill_total > 100 and bill_total < 200:
    print("Bill is more then 100.")
    bill_total = bill_total - discount1
elif bill_total > 200:
    print("Bill is more then 200.")
    bill_total = bill_total - discount2
else:
    print("Bill is less then 100.")



print("Total bill: " + str(bill_total))

