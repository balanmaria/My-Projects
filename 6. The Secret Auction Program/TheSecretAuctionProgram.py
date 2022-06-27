from replit import clear
from Beginner.Day9.art import logo

print(logo)
print("Welcome to the secret auction program.")

end_of_person=False

person={}

def find_highest_bidder(bidding_record):
    max=-1
    pers=""
    for i in bidding_record:
        bid_amount=bidding_record[i]
        if bid_amount > max:
            max=bid_amount
            pers=i
    print(f"The winner is {pers} with a bid of ${max}!")

while not end_of_person:
    name=input("Which is your name?: ")
    bid=int(input("What's your bid?: $"))
    person[name]=bid
    answer=input("Are there any other bidders? Type 'yes' or 'no'. ")
    if answer == "no":
        end_of_person=True
        find_highest_bidder(person)
    elif answer == "yes":
        clear()
