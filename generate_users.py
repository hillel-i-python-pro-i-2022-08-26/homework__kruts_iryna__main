from faker import Faker

fake = Faker()


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} {self.email}"


def generate_list_of_person(rand_amt: int):
    """
    Функция-генератор для случайных фейковых имен и емеилов
    :return: Рандомное количество имен и емеилов
    """
    yield [Person(fake.first_name(), fake.email()).__str__() for _ in range(100)][
        : rand_amt + 1
    ]
