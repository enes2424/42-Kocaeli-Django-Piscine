import sys


def printCapitalCity(state):
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }

    try:
        print(capital_cities[states[state]])
    except KeyError:
        print("Unknown state")


def main():
    if len(sys.argv) != 2:
        return

    state = sys.argv[1]

    printCapitalCity(state)


if __name__ == "__main__":
    main()
