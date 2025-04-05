# Используем официальный slim-образ Python для уменьшения размера
FROM python:3.11-slim-bullseye as builder

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

# Устанавливаем системные зависимости, необходимые для Python и SQLite
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# Финальный образ
FROM python:3.11-slim-bullseye

WORKDIR /app

# Копируем установленные зависимости из builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app .

# Добавляем пути к Python PATH
ENV PATH=/root/.local/bin:$PATH

# Настройки среды Django
# ENV DJANGO_SETTINGS_MODULE=your_project.settings.production
# ENV DEBUG=False
# ENV ALLOWED_HOSTS=*

# Копируем исходный код приложения
COPY . .

# Собираем статические файлы
RUN python manage.py collectstatic --noinput --clear

# # Применяем миграции (в реальном продакшене лучше делать через entrypoint)
# RUN python manage.py migrate --noinput

# Открываем порт и запускаем сервер
EXPOSE 8000