from api_client import (
    check_api_connection,
)  # импортируем функцию для проверки соединения с API

"""Основная функция запуска приложения"""


def main():
    if check_api_connection():
        print("Соединение с API успешно установлено.")
        ### основной код
    else:
        print(
            "Не удалось установить соединение с API. Проверьте ваше интернет-соединение или доступность API."
        )


if __name__ == "__main__":
    main()
