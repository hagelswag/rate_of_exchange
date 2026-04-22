import logging  # импорт модуля логирования
from logging_config import logging_setup  # импорт настроек логирования
from api_client import (
    check_api_connection,
)  # импортируем функцию для проверки соединения с API


"""Основная функция запуска приложения"""


def main():
    logging_setup()  # вызываем функцию для настройки логирования
    if check_api_connection():
        logging.info(
            "Соединение с API успешно установлено."
        )  # логируем успешное соединение
        print("Соединение с API успешно установлено.")
        ### основной код
    else:
        print(
            "Не удалось установить соединение с API. Проверьте ваше интернет-соединение или доступность API."
        )


if __name__ == "__main__":
    main()
