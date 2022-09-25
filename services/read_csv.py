import csv
import pathlib


def calculate_csv() -> str:
    """
    Функция для считывания файла csv
    :return: средний рост, средний вес
    """
    ROOT_PATH = pathlib.Path(__file__).parents[1]
    # path to location to our file
    FILES_PATH = ROOT_PATH.joinpath("data")
    with open(FILES_PATH.joinpath("people_data.csv")) as csv_file:
        reader = csv.DictReader(csv_file)
        sum_of_height = 0
        sum_of_weight = 0
        amount = 0
        for i in reader:
            sum_of_height += float(i[' "Height(Inches)"'])
            sum_of_weight += float(i[' "Weight(Pounds)"'])
            amount += 1
        return f"Average of height = {round(sum_of_height / amount, 2)}, Average of weight = {round(sum_of_weight / amount, 2)} "
