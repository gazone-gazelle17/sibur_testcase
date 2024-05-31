# Sibur testcase

Testcase solution for Sibur.

## Описание

Тестовое задание для Sibur.
Основная логика содержится в файле main.py, отдельные логические блоки в файлах aggregator.py, vabus.py, event.py и metric.py.
Файл example.env содержит пример переменных окружения, в файле problems_and_solutions.txt содержится описание возможных проблем в сервисе, путей их решения и потенциального развития сервиса.

## Установка и запуск

### Клонирование репозитория

```bash
git clone git@github.com:gazone-gazelle17/sibur_testcase.git
cd sibur_testcase
```

### Установка зависимостей

```bash
poetry install
```

### Настройка переменных окружения

При необходимости отредактируйте содержимое файла example.env, затем скопируйте файл `example.env` в `.env` следующей командой:
```bash
cp example.env .env
```

### Запуск сервиса

```bash
poetry run python main.py
```

### Использование Docker

#### Соберите Docker-образ

```bash
docker build -t sibur_testcase .
```

#### Запустите Docker-контейнер

```bash
docker run --env-file .env sibur_testcase
```

### Предупреждение
На прошедшей неделе Docker прекратил поддержку IP-адресов в России, поэтому при работе могут возникнуть сложности. В частности, при логине в Docker может возникнуть ошибка 403. Решение, которое использовал я - работать без входа в Docker, подсмотрел тут:
<https://habr.com/ru/articles/818527/comments/>

### Переменные окружения

- VABUS_URL: URL для подключения к шине данных VaBus.
- AGGREGATION_INTERVAL: Интервал агрегации событий в секундах.
- STORAGE_TYPE: Тип хранилища для агрегированных событий (postgres или kafka).
- POSTGRES_DB: Имя базы данных PostgreSQL.
- POSTGRES_USER: Имя пользователя PostgreSQL.
- POSTGRES_PASSWORD: Пароль пользователя PostgreSQL.
- POSTGRES_HOST: Хост PostgreSQL.
- POSTGRES_PORT: Порт PostgreSQL.
- KAFKA_BROKER_URL: URL брокера Kafka.
- KAFKA_TOPIC: Название топика Kafka.

## Автор
Александр Гасымов