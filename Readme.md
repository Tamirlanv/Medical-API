# Medical API
![homepageUI.png](docs/homepageUI.png)

Простое веб-приложение для просмотра и записи на приём к врачу. git rm --cached backend/test_main.http

UI проекта можно увидеть в папке docs  
Проект адаптирован для запуска через **Docker**.

---

## ⚙️ Стек технологий
**Backend:** FastAPI, pydantic, asyncio, ...  
**Frontend:** React, ant design, tailwind, ...  

---

### 🐳 Запуск через Docker

Проект собран в виде готовых Docker-образов:

- Backend: `tamirvlad/medapiback`  
- Frontend: `tamirvlad/medapifront`  

Для запуска скопируйте содержимое docker-compose.yml, откройте новую папку в VS Code создайте данный файл и вставьте содержимое.

После запуска откройте:
- http://localhost:5174 — фронтенд  
- http://localhost:8000/docs — API-документация  

---

## Docker
- **Docker Hub** [tamirvlad](https://hub.docker.com/repositories/tamirvlad)

