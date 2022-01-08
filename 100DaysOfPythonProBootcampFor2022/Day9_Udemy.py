# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades = {}
# for student in student_scores:
#   if student_scores[student] > 90:
#     student_grades[student] = "Outstanding"
#   elif student_scores[student] > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif student_scores[student] > 70:
#     student_grades[student] = "Acceptable"
#   elif student_scores[student] < 70:
#     student_grades[student] = "Fail"
#
# print(student_grades)
#
#
# travel_log = {
#   "France": {"cities_visited" :["Paris", "Lille" , "Dijon"]  , "total_visits": 12},
#   "Gremany" : {"cities_visited" :["Berlin", "Hamburg" , "Stutthart"] , "total_visits": 2} ,
# }
#
# cities_visited = {
#   "Paris": 3 ,
#   "Lille": 1 ,
#   "Dijon": 1 ,
#
# }
# print(travel_log)
# from replit import clear
# # HINT: You can call clear() to clear the output in the console.
# from art import logo
#
# print(logo)
# still_biding = True
# total_bids = {}
#
#
# def new_bid():
#   name = input("what is you name?:")
#   bid = int(input("What's your bid:$"))
#   total_bids[name] = bid
#
#
# def higiset_bid():
#   max_bid = 0
#   for bider in total_bids:
#     temp_bid = total_bids[bider]
#     if max_bid < temp_bid:
#       max_bid = temp_bid
#       temp_bider = bider
#
#   print(f"The winner is {temp_bider} with bid of ${max_bid}")
#
#
# while still_biding:
#   user_input = input(
#     "Where is some one else that whant to bid ? 'Yes' or 'No'").lower()
#   if user_input == "yes":
#     new_bid()
#     clear()
#   elif user_input == "no":
#     print(total_bids)
#     higiset_bid()
#     still_biding = False

from replit import clear
from art_Day9 import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
