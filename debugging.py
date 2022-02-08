def divisor(num):

    divisor = [i for i in range(1, num + 1) if num % i == 0]

    return divisor


def run():

    try:

        num = int(input("ingresa un numero "))
        if num < 0:
            raise ValueError()
        print(divisor(num))

    except ValueError:
        print("No se permiten números negativos o letras")


if __name__ == "__main__":
    run()
