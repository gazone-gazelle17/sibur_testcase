# Использует образ Python 3.9
FROM python:3.9-slim

# Устанавливает рабочую директорию
WORKDIR /app

# Копирует файл с зависимостями
COPY requirements.txt .

# Устанавливает зависимости
RUN pip install -r requirements.txt --no-cache-dir

# Копирует все файлы в контейнер
COPY . .

# Запускает приложение
CMD ["python3", "main.py"]