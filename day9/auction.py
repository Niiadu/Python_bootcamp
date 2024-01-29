new_bidder = False
bidder = {}

def highest_bidder(bidder):
    highest_bid = 0
    winner = ""
    for bid in bidder :
        bid_amount = bidder[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f"The winner is {winner}, with a bid of ${highest_bid}")

while not new_bidder:
    name = input("Whats your name? ")
    price = int(input("Whats your bidding price $"))
    
    bidder[name] = price
    print(bidder)
    other_bidder = input("Are there any more bidders? Type 'yes' or 'no'. ").lower()
    if other_bidder == "yes":
        new_bidder = False
    else:
        new_bidder = True
        highest_bidder(bidder)
        
