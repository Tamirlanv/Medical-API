export const getSlots = async () => {
    const res = await fetch("http://localhost:8000/slots/");
    return await res.json();
};