import { useEffect, useState } from "react";
import { Card, Spin } from "antd";

const DoctorsPage = () => {
    const [doctors, setDoctors] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch("http://localhost:8000/doctors/")
            .then(res => res.json())
            .then(data => {
                setDoctors(data);
                setLoading(false);
            });
    }, []);

    if (loading) return <Spin size="large" className="mt-10" />;

    return (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 p-4">
            {doctors.map(doc => (
                <Card key={doc.id} title={doc.name} bordered className="shadow-md">
                    <p><b>Специальность:</b> {doc.specialty}</p>
                    <p>{doc.bio}</p>
                </Card>
            ))}
        </div>
    );
};

export default DoctorsPage;
