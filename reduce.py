from functools import reduce


def run():
    my_list = [2, 2, 2, 2, 2, 2]

    reduces = reduce(lambda a, b: a*b, my_list)

    print(reduces)


if __name__ == "__main__":
    run()
