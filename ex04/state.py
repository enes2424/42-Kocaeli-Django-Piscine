import sys


def printState(capital_city):
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }

    try:
        state_abbr = next(
            key for key, value in capital_cities.items() if value == capital_city
        )
        state_name = next(key for key, value in states.items() if value == state_abbr)
        print(state_name)
    except StopIteration:
        print("Unknown capital city")


def main():
    if len(sys.argv) != 2:
        return

    capital_city = sys.argv[1]

    printState(capital_city)


if __name__ == "__main__":
    main()
