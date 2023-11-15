# List of names
names = ["Sultan", "Sanu", "Jose", "Sahil", "Fudail"]

# Define a personalized message template
message_template = "Hello, {}! Thank you for being awesome."

# Print personalized messages for each person
for name in names:
    personalized_message = message_template.format(name)
    print(personalized_message)
