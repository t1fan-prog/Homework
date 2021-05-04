country_name = input("Enter country's name:\n")
country_capital = input("Enter country's capital:\n")


def make_country(name, capital):
    out_dict = dict([(name, capital)])
    print(out_dict)


make_country(country_name, country_capital)
