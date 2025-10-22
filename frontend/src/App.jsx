import React from "react";
import { Layout, Menu } from "antd";
import { HomeOutlined, TeamOutlined, CalendarOutlined } from "@ant-design/icons";
import { Routes, Route, useNavigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import DoctorsPage from "./pages/DoctorsPage";
import BookingPage from "./pages/BookingPage";

const { Sider, Content } = Layout;

const App = () => {
    const navigate = useNavigate();

    const menuItems = [
        { key: "/", icon: <HomeOutlined />, label: "Главная" },
        { key: "/doctors", icon: <TeamOutlined />, label: "Врачи" },
        { key: "/booking", icon: <CalendarOutlined />, label: "Записаться" },
    ];

    return (
        <Layout style={{ minHeight: "100vh" }}>
            <Sider width={250} style={{ background: "#fff" }}>
                <Menu
                    mode="inline"
                    defaultSelectedKeys={["/"]}
                    onClick={(e) => navigate(e.key)}
                    items={menuItems}
                    style={{ height: "100vh" }}
                />
            </Sider>

            <Layout style={{ background: "#f9f9f9" }}
                    className="h-screen overflow-y-scroll">
                <Content style={{ padding: "24px" }}>
                    <Routes>
                        <Route path="/" element={<HomePage />} />
                        <Route path="/doctors" element={<DoctorsPage />} />
                        <Route path="/booking" element={<BookingPage />} />
                    </Routes>
                </Content>
            </Layout>
        </Layout>
    );
};

export default App;
