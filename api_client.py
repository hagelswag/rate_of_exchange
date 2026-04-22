import requests  # будем делать HTTP запросы к API для получения данных о курсах валют
import os  # в данном случае нужен для передачи ключа из .env файла в виде переменной окружения
from dotenv import load_dotenv  # нужен для загрузки переменных окружения из .env файла

load_dotenv()  # загружаем переменные окружения из .env файла

API_BASE_URL = os.getenv("API_BASE_URL")  # получили ключ из .env файла


"""Функция для проверки соединения с API"""


def check_api_connection():
    try:
        response = requests.get(
            f"{API_BASE_URL}/USD?parammode=2", timeout=5
        )  # делаем запрос к API для проверки соединения
        response.raise_for_status()  # если не 200 то вызывает исключение HTTPError
        return True  # если запрос успешный, возвращаем True
    except (
        requests.exceptions.RequestException
    ):  # используем RequestsException для всех ошибок (на случай если нет интернета или API недоступно)
        return False
