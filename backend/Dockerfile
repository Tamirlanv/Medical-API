# Stage 1: Build
FROM python:3.12-slim AS build
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# Копируем весь код
COPY src/ ./src
COPY .env ./.env   

# Stage 2: Runtime
FROM python:3.12-slim
WORKDIR /app

# Копируем зависимости и код
COPY --from=build /install /usr/local
COPY --from=build /app/src /app/src
COPY --from=build /app/.env ./

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
