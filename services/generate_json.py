import json

import requests


def generate_json(url) -> str:
    """
    Функция для обработки файла json
    :return: Количество и имена космонавтов в настоящий момент
    """
    response = requests.get(url)
    with open("../astronauts.json", "w") as f:
        json.dump(response.json(), f, indent=2)
    with open("../astronauts.json", "r") as f:
        data = json.load(f)
    return data["people"]
