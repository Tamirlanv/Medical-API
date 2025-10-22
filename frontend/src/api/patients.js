export const bookSlot = async (slotId) => {
    const res = await fetch("http://localhost:8000/patients/book", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ slot_id: slotId }),
    });
    return await res.json();
};