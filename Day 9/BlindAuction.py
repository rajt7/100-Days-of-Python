flag = True
dict = {}

def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if(bid_amount > highest_bid):
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of {highest_bid}.")

while(flag):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dict[name] = bid
    
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if(other_bidders == 'no'):
        flag = False
        find_highest_bidder(dict)