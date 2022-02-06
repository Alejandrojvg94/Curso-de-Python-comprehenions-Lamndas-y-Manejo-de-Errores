DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
        'old': True},
    {
        'name': 'Luisana', 'age': 33, 'organization': 'Globant',
        'position': 'UX Designer', 'language': 'javascript', 'old': False},
    {
        'name': 'Héctor', 'age': 19, 'organization': 'Platzi',
        'position': 'Associate', 'language': 'ruby', 'old': False},
    {
        'name': 'Gabriel', 'age': 20, 'organization': 'Platzi',
        'position': 'Associate', 'language': 'javascript', 'old': False},
    {
        'name': 'Isabella', 'age': 30, 'organization': 'Platzi',
        'position': 'QA Manager', 'language': 'java', 'old': False},
    {
        'name': 'Karo', 'age': 23, 'organization': 'Everis',
        'position': 'Backend Developer', 'language': 'python', 'old': False},
    {
        'name': 'Ariel', 'age': 32, 'organization': 'Rappi',
        'position': 'Support', 'language': '', 'old': False},
    {
        'name': 'Juan', 'age': 17, 'organization': '',
        'position': 'Student', 'language': 'go', 'old': False},
    {
        'name': 'Pablo', 'age': 32, 'organization': 'Master',
        'position': 'Human Resources Manager', 'language': 'python', 'old': False},
    {
        'name': 'Lorena', 'age': 56, 'organization': 'Python Organization',
        'position': 'Language Maker', 'language': 'python', 'old': False}
]


# Lista = []


def run():

    all_python_devs = list(
        filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_devs = list(
        map(lambda worker: worker["name"], all_python_devs))

    # for worker in all_platzi_devs:
    #     Lista.append(worker)

    # print(Lista)

    all_platzi_workers = list(
        filter(lambda worker: worker["language"] == "python", DATA))
    all_platzi_workers = list(
        map(lambda worker: worker["name"], all_platzi_workers))

    # for worker in all_platzi_workers:
    #     print(worker)

    old_people = [worker["name"] for worker in DATA if worker["age"] > 70]

    # print(old_people)

    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]

    print(adults)


if __name__ == "__main__":
    run()
