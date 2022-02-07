import random
import os

os.system("clear")
print("¡Adivina la palabra!")
word = []
answer = {}
print(answer)
di = {}


def read_data():

    with open("./Archivos/data.txt", "r", encoding="utf-8") as d:
        for i in d:
            i = i.strip("\n")
            word.append(i)
        return random.choice(word)


rand = read_data()
print(rand)


def ciclo():
    answer_values = answer.values()
    answer_values = list(answer_values)
    answer_values = "".join(answer_values)
    return answer_values


def dics():

    for i in list(enumerate(rand)):
        k = i[0]
        v = i[1]
        di[k] = v
    for i in di:

        for j in range(0, i+1):
            z = di.get(j)

        lyrics = input("Ingresa una letra, por favor: ")
        while lyrics != z:
            lyrics = input("Ingresa una letra, por favor: ")
            print(answer, "prueb", rand)

            if lyrics == z:
                answer[j] = z


def run():
    read_data()
    dics()
    ciclo()


if __name__ == "__main__":
    run()
