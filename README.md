# Currency Converter (CLI)

A command-line tool for real-time currency conversion using an external API and a caching mechanism.

## Features

- Currency conversion between different base and target currencies.
- Real-time exchange rates via ExchangeRate-API.
- Data caching in `cache.json` (updated every 24 hours to reduce API calls).
- Validation for currency codes (ISO 4217) and numeric amounts.
- Comprehensive handling of network and API exceptions.

## Installation and Execution (Local)

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the application**:
    ```bash
    python src/main.py
    ```
3.  **Run tests**:
    ```bash
    pytest tests/
    ```

## Running with Docker

1.  **Build the image**:
    ```bash
    docker build -t currency-converter .
    ```
2.  **Run the container**:
    ```bash
    docker run -it -v "$(pwd)/data:/app/data" currency-converter:latest
    ```

---

# Конвертер валют (CLI)

Программа для конвертации валют в реальном времени с использованием внешнего API и механизмом кэширования.

## Функционал

- Конвертация суммы из одной валюты в другую.
- Получение актуальных курсов через ExchangeRate-API.
- Кэширование данных в `cache.json` (обновление раз в 24 часа для экономии трафика и запросов).
- Валидация кодов валют (ISO 4217) и вводимых сумм.
- Обработка сетевых ошибок и исключений API.

## Установка и запуск (Локально)

1.  **Установка зависимостей**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Запуск**:
    ```bash
    python src/main.py
    ```
3.  **Тестирование**:
    ```bash
    pytest tests/
    ```

## Запуск через Docker

1.  **Сборка**:
    ```bash
    docker build -t currency-converter .
    ```
2.  **Запуск**:
    ```bash
    docker run -it -v "$(pwd)/data:/app/data" currency-converter:latest
    ```
