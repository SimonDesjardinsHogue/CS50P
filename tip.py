def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    # Accept a str
    # Formated ##.##
    # Remove leading $
    # return as a float

    dnosign = d.lstrip("$")
    return float(dnosign)


def percent_to_float(p):
    # TODO
    # Accept a str
    # Formated ##.##
    # Remove ending %
    # return as a float

    pnosign = p.rstrip("%")
    return float(pnosign) / 100


main()
