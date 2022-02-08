def divisor(num):

    divisor = [i for i in range(1, num + 1) if num % i == 0]

    return divisor


def run():

    num = input("ingresa un numero ")

    assert int(num) > 0, "SOlo numeros positivos"
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisor(int(num)))


if __name__ == "__main__":
    run()
