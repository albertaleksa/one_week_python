print("WELCOME TO OUR USELESS STORE!")
print("*" * 29)
item = input("what item are you purchasing? ")
price = float(input(f"what is the price of {item}? "))
count = int(input(f"how many {item} are you buying? "))

print()
print(f"Added {count} {item}(s) to shopping cart")
print(f"Subtotal: ${price * count}")
