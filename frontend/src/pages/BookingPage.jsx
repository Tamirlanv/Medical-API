import { useEffect, useState } from "react";
import { Card, Modal, Button, Spin } from "antd";

const BookingPage = () => {
    const [slots, setSlots] = useState([]);
    const [selected, setSelected] = useState(null);
    const [loading, setLoading] = useState(true);
    const [isBookedConfirmed, setIsBookedConfirmed] = useState(false);

    // Загружаем слоты
    useEffect(() => {
        fetch("http://localhost:8000/slots/")
            .then(res => res.json())
            .then(data => {
                console.log("SLOTS RESPONSE:", data);
                setSlots(data);
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setLoading(false);
            });
    }, []);

    if (loading) return <Spin size="large" className="mt-10" />;

    // Функция бронирования
    const handleBooking = async () => {
        try {
            const patientId = 1; // <-- сюда передавай реальный ID пациента
            const res = await fetch("http://localhost:8000/bookings/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ slot_id: selected.id, patient_id: patientId }),
            });

            if (!res.ok) throw new Error("Ошибка при бронировании");

            await res.json();

            // Обновляем локальный стейт слотов
            setSlots(prev =>
                prev.map(slot =>
                    slot.id === selected.id ? { ...slot, is_booked: true } : slot
                )
            );

            // Показываем подтверждение в модале
            setIsBookedConfirmed(true);

        } catch (err) {
            console.error(err);
            Modal.error({ title: "Не удалось записаться", content: err.message });
        }
    };

    return (
        <>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 p-4">
                {slots.map(slot => (
                    <Card
                        key={slot.id}
                        className={`shadow-md hover:shadow-xl cursor-pointer ${
                            slot.is_booked ? "opacity-50 cursor-not-allowed" : ""
                        }`}
                        onClick={() => !slot.is_booked && setSelected(slot)}
                    >
                        <p><b>Врач:</b> {slot.doctor.name}</p>
                        <p><b>Время:</b> {new Date(slot.start_time).toLocaleString()}</p>
                        {slot.is_booked && <p className="text-red-500 font-bold">Занято</p>}
                    </Card>
                ))}
            </div>

            <Modal
                title="Запись на приём"
                open={!!selected}
                onCancel={() => {
                    setSelected(null);
                    setIsBookedConfirmed(false);
                }}
                footer={null}
            >
                {selected && !isBookedConfirmed && (
                    <div>
                        <p><b>Врач:</b> {selected.doctor.name}</p>
                        <p><b>Дата и время:</b> {new Date(selected.start_time).toLocaleString()}</p>
                        <Button
                            type="primary"
                            block
                            onClick={handleBooking}
                        >
                            Подтвердить запись
                        </Button>
                    </div>
                )}

                {selected && isBookedConfirmed && (
                    <div className="text-center">
                        <p className="text-green-600 font-bold text-lg">✅ Вы успешно записаны!</p>
                        <Button
                            type="default"
                            block
                            className="mt-4"
                            onClick={() => {
                                setSelected(null);
                                setIsBookedConfirmed(false);
                            }}
                        >
                            Закрыть
                        </Button>
                    </div>
                )}
            </Modal>
        </>
    );
};

export default BookingPage;
