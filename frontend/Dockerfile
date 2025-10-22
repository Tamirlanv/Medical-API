# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости чисто
RUN npm ci

# Копируем исходники
COPY . .

# Собираем Vite проект
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine
WORKDIR /usr/share/nginx/html

# Чистим default содержимое
RUN rm -rf ./*

# Копируем только собранную статику
COPY --from=builder /app/dist .

# Экспонируем порт
EXPOSE 80

# Запуск Nginx
CMD ["nginx", "-g", "daemon off;"]



