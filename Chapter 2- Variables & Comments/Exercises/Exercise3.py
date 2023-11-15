name_with_whitespace = "\t Syed ruwaiz hussain \n"


print(name_with_whitespace)


name_stripped_left = name_with_whitespace.lstrip()
name_stripped_right = name_with_whitespace.rstrip()
name_stripped_both = name_with_whitespace.strip()

print("Using lstrip():", name_stripped_left)
print("Using rstrip():", name_stripped_right)
print("Using strip():", name_stripped_both)