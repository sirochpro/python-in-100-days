from bidding_art import logo

print(logo)
print("Welcome to the secret auction program.")

continue_game = True

bids = {}

while continue_game:
    name = input("What is your name?: ")
    price = input("What's you bid?: ")

    bids[name] = price

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n".lower())
    if other_bidders == "yes":
        continue_game = True
        print("\n" * 20)
    elif other_bidders == "no":
        bid_name = ""
        bid_value = 0
        for key in bids:
            bid = int(bids[key])
            if int(bid) > bid_value:
                bid_value = bid
                bid_name = key
        print(f"The winner is {bid_name} with a bid of ${bid_value}.")
        continue_game = False
    else:
        print("Invalid option!")

