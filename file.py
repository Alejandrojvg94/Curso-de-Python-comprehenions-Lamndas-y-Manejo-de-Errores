import numbers


def read():
    numbers = []

    with open("./Archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)


def write():
    names = ["Facundo", "Godinez", "Armando", "Rodrigo", "ROcío"]

    with open("./Archivos/names.txt", "w", encoding="utf-8") as n:

        for name in names:
            n.write(name)
            n.write("\n")


def run():
    write()


if __name__ == "__main__":
    run()
