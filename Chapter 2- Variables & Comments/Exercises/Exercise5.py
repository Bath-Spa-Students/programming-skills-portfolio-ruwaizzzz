# Cost of each USB stick and total budget
usb_stick_cost = 6
total_budget = 50

# Calculate the maximum number of USB sticks she can buy
num_usb_sticks = total_budget // usb_stick_cost

# Calculate the amount of money left after buying the USB sticks
money_left = total_budget % usb_stick_cost

# Display the results
print(f"With £{total_budget}, she can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{money_left} left.")
