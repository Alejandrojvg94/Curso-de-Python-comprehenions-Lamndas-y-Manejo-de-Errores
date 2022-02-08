import random
import os


def read_data(file_data="./Archivos/data.txt"):
    word = []
    with open(file_data, "r", encoding="utf-8") as d:
        for i in d:
            word.append(i.strip().upper())
    return word


def dics():
    data = read_data(file_data="./Archivos/data.txt")
    rand = random.choice(data)
    rand_list = [letter for letter in rand]
    rand_list_underscores = ["_"] * len(rand_list)
    letter_index_dic = {}

    for idx, letter in enumerate(rand):
        if not letter_index_dic.get(letter):
            letter_index_dic[letter] = []
        letter_index_dic[letter].append(idx)

    while True:
        print("¡Adivina la palabra! ")

        os.system("clear")
        for element in rand_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in rand_list:
            for idx in letter_index_dic[letter]:
                rand_list_underscores[idx] = letter

        if "_" not in rand_list_underscores:
            # Si estÃ¡s en Unix (Mac o Linux) cambia cls por clear
            os.system("clear")
            print("¡Ganaste! La palabra era", rand)
            break


def run():
    read_data()
    dics()


if __name__ == "__main__":
    run()
