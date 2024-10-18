'''Auction Dictionary Project for Day 9'''

LOGO = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(LOGO)

bids = {}
bidding_active = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while bidding_active:
    name = input("What is your name: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    shouldcontinue = input("Are there any other bidders? Type yes or no.").lower()
    if shouldcontinue == "yes":
        print("\n" * 20)
    elif shouldcontinue == "no":
        bidding_active = False
        find_highest_bidder(bids)
