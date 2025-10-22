import logging
import random
from datetime import datetime, timedelta
from sqlalchemy import select, delete
from src.models.doctors import Doctor
from src.models.appointment_slots import AppointmentSlot
from src.models.bookings import Booking
from src.database import AsyncSessionLocal

logger = logging.getLogger(__name__)

# Генерация случайных слотов
def generate_random_slots(start_hour=8, end_hour=18, slot_length=20, days=5, slots_per_day=2):
    slots = []
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    for day_offset in range(days):
        day_start = base_date + timedelta(days=day_offset)
        available_minutes = list(range(0, (end_hour - start_hour) * 60, slot_length))
        random.shuffle(available_minutes)
        chosen_times = sorted(available_minutes[:slots_per_day])

        for minute_offset in chosen_times:
            start_time = day_start.replace(hour=start_hour, minute=0) + timedelta(minutes=minute_offset)
            end_time = start_time + timedelta(minutes=slot_length)
            slots.append((start_time, end_time))
    return slots


async def clear_booking_table(session):
    logger.info("🧨 Очищаем все записи в таблице Booking...")
    await session.execute(delete(Booking))
    await session.commit()
    logger.info("✅ Все записи Booking удалены")


async def seed_slots(session: AsyncSessionLocal):
    # 🧨 Очищаем таблицу Booking
    await clear_booking_table(session)

    # 🧨 Удаляем старые слоты
    logger.info("🧨 Удаляем старые слоты...")
    await session.execute(delete(AppointmentSlot))
    await session.commit()
    logger.info("🧹 Старые слоты удалены.")

    # Получаем докторов
    result = await session.execute(select(Doctor))
    doctors = result.scalars().all()

    if not doctors:
        logger.warning("⚠️ Нет докторов для создания слотов.")
        return

    logger.info(f"🕒 Генерируем по 2 слота в день (5 дней) для {len(doctors)} докторов...")

    for doctor in doctors:
        times = generate_random_slots()
        for start_time, end_time in times:
            slot = AppointmentSlot(
                doctor_id=doctor.id,
                start_time=start_time,
                end_time=end_time,
                is_booked=False,
            )
            session.add(slot)
        logger.info(f"✅ Слоты созданы для {doctor.name}")

    await session.commit()
    logger.info("📦 Все слоты успешно сохранены в базе.")
