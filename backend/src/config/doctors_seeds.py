import logging
from src.models.doctors import Doctor
from sqlalchemy import select

logger = logging.getLogger(__name__)

doctors_data = [
    {"name": "Айдана Сулейменова", "specialty": "therapist", "bio": "Опытный терапевт с 10-летним стажем."},
    {"name": "Нурлан Ахметов", "specialty": "cardiologist", "bio": "Кардиолог, специализируется на аритмиях."},
    {"name": "Светлана Ким", "specialty": "dentist", "bio": "Стоматолог, работает с детьми и взрослыми."},
    {"name": "Ержан Тлеубаев", "specialty": "therapist", "bio": "Терапевт, специализируется на хронических заболеваниях."},
    {"name": "Алия Жумагалиева", "specialty": "cardiologist", "bio": "Кардиолог с акцентом на профилактику заболеваний."},
    {"name": "Руслан Токтаров", "specialty": "dentist", "bio": "Специалист по эстетической стоматологии."},
]

async def seed_doctors(session):
    result = await session.execute(select(Doctor))
    existing = result.scalars().all()
    if existing:
        logger.info("⚠️ Доктора уже сидированы, пропускаем.")
        return

    for doc in doctors_data:
        doctor = Doctor(**doc)
        session.add(doctor)
        logger.info(f"👨‍⚕️ Добавлен доктор: {doc['name']} ({doc['specialty']})")

    await session.commit()
    logger.info("📦 Все доктора успешно сохранены в базе.")
