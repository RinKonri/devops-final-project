# Используем официальный образ Python
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Запускаем приложение
CMD ["python", "app.py"]