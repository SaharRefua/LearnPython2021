print("Welcome to tip calculator ")
bill = input("What was the total bill? $")
percentage =input("What Percentage tip would you like to give? 10 ,12 ,15 ")
people_split_bill=input("How many people to split the bill ? ")
# percentage_as_float=int(percentage)/100
# percentage_as_float+=1
# total_bill=float(bill)*percentage_as_float
# my_bill=total_bill/int(people_split_bill)
total_tip_amount = (1+int(percentage)/100) * float(bill)
bill_pre_preson = total_tip_amount/int(people_split_bill)
#final_bill=round(bill_pre_preson,2)
final_bill="{:.2f}".format(bill_pre_preson)

print(f"Each person should pay: ${final_bill}")