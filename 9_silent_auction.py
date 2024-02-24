import subprocess
import time
logo = '''
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

bids = {}
auction_open = True
print(logo)
print("Welcome to the silent auction.")
while auction_open:
    name = input("What is your name?\n")
    if name in bids:
        print("Someone with that name has already bid, please choose a different name, or include your last name:")
    else:
        while True:
            bid_input = input("What's your bid?\n$")
            try:
                bid = int(bid_input)  # Attempt to convert bid to integer
                bids[name] = bid
                break
            except ValueError:
                print("Please input a whole number.")
                
        more_bids = input("Are there any other bidders? (y/n)\n").lower()
        if more_bids == "n":
            print("Thank you, the auction is now closed.")
            time.sleep(0.5)
            auction_open = False
        elif more_bids == 'y':
            subprocess.call('cls', shell=True)

highest_bid = 0
winner = ""
for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winnner of the aucition is {winner} with the highest bid of ${highest_bid}!!")
input("Hit enter to close this window.")
