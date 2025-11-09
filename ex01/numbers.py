def print_numbers():
    file = open("numbers.txt", "r")
    numbers = file.readlines()[0].split(",")
    for number in numbers:
        try:
            print(int(number))
        except ValueError:
            pass
    file.close()


if __name__ == "__main__":
    print_numbers()
