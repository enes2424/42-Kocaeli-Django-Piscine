import sys


def printStatus(elm):
    if elm == "":
        return

    region = elm.lower()

    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }

    for state, abbr in states.items():
        if region == state.lower():
            capital_city = capital_cities[abbr]
            print(f"{capital_city} is the capital city of {state}")
            return

    for abbr, capital_city in capital_cities.items():
        if region == capital_city.lower():
            state = next(key for key, value in states.items() if value == abbr)
            print(f"{capital_city} is the capital city of {state}")
            return

    print(f"{elm} is neither a capital city nor a state")


def main():
    if len(sys.argv) != 2:
        return

    arr = sys.argv[1].split(",")

    for elm in arr:
        printStatus(elm.strip())


if __name__ == "__main__":
    main()
