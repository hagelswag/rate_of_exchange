import logging

"""Настройки логирования"""


def logging_setup():
    logging.basicConfig(  # конфигурация логирования
        filename="app.log",  # имя файла для логов
        format="%(asctime)s - %(levelname)s - %(message)s",  # формат логов
        level=logging.INFO,  #
        encoding="utf-8",  # кодировка для логов (для поддержки кириллицы)
    )
