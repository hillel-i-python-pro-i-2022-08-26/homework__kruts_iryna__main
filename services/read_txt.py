import pathlib
from typing import List


def read_txt() -> List[str]:
    """
    Функция для вывода данных из txt файла
    :return: Список со строками
    """
    # path to root of the file
    ROOT_PATH = pathlib.Path(__file__).parents[1]
    # path to location to our file
    FILES_PATH = ROOT_PATH.joinpath("data")
    with open(FILES_PATH.joinpath("poem.txt"), "r") as reader:
        return reader.readlines()
