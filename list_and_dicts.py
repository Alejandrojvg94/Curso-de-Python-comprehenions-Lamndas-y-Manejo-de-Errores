from re import X


def run():
    my_list = [1, "hello", True, 4, 5]
    my_dict = {"firstname": "Alejandro", "lastname: ": "Velasco"}
    list_natural = []

    super_list = [
        {"firstname": "Alejandro", "lastname: ": "Velasco"},
        {"firstname": "Jhonny", "lastname: ": "Gómez"},
        {"firstname": "Javier", "lastname: ": "Velasco"},
        {"firstname": "Guiancarlo", "lastname: ": "Gomez"}

    ]
    for x in super_list:
        # print(x)
        pass

    super_dirt = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, -0, 1],
        "foating_nums": [1.1, 2.3, 3, 1.09]
    }

    for key, value in super_dirt.items():
        # print(key, "_", value)
        pass

    for x in range(0, 101):
        list_natural.append(x**2)

    print(list_natural)


if __name__ == "__main__":
    run()
