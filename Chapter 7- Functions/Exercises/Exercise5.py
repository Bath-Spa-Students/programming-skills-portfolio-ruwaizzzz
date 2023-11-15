def describe_city(city, country='india'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('chennai')
describe_city('dubai', 'uae')
describe_city('hyderabad')