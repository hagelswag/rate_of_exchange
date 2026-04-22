import logging
import requests  # будем делать HTTP запросы к API для получения данных о курсах валют
import os  # в данном случае нужен для передачи ключа из .env файла в виде переменной окружения
from dotenv import (
    load_dotenv,
)  # достает данные из .env и помещает в перемененые окружения ос

load_dotenv()  # загружаем переменные окружения из .env файла

API_BASE_URL = os.getenv("API_BASE_URL")  # получили ключ из .env файла


"""Функция для проверки соединения с API"""


def check_api_connection():
    try:
        response = requests.get(
            f"{API_BASE_URL}/USD?parammode=2", timeout=5
        )  # делаем запрос к API для проверки соединения, добавляем таймаут чтобы не уйти в бесконечное ожидание
        response.raise_for_status()  # если код 4хх или 5хх то вызывает исключение HTTPError
        return True  # если запрос успешный, возвращаем True
    except (
        requests.exceptions.RequestException
    ) as e:  # используем RequestsException для всех ошибок (на случай если нет интернета, превышения времени ожидания или API недоступно)
        logging.error(
            f"Ошибка при попытке соединения с API: {e}"
        )  # логируем конкретную ошибку
        return False
