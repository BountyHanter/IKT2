# Используйте официальный образ Python 3.10 как родительский образ
FROM python:3.10-slim-buster

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте файлы проекта в рабочую директорию
COPY . /app

# Установите зависимости
RUN pip install --no-cache-dir -r req.txt

# Откройте порт 49443 для связи с контейнером
EXPOSE 49443

# Запустите приложение
CMD ["mkdocs", "serve", "-a", "0.0.0.0:49443"]