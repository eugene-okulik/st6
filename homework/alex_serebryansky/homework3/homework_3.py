from math import ceil

name = input("Enter your name: ")
wish = input("What do you want to buy?: ")
price = int(input("How much $ is it cost?: "))
amount = int(input("How much money do you have?: "))
economy = int(input("How much money can you save per month?: "))

print(f"\nHello, {name}! You don't have {price - amount}$ to buy a {wish}\n\n"
      f"Purchase option: {amount > price}\n\n"
      f"{ceil((price - amount) / economy)} months left until purchase!"
      )
