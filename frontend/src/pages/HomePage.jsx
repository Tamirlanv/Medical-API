const HomePage = () => (
    <div className="flex flex-col justify-center items-center h-full text-center">
        <img
            src="https://cdn-icons-png.flaticon.com/512/2966/2966327.png"
            alt="clinic"
            className="w-32 mb-4"
        />
        <h1 className="text-3xl font-bold text-blue-700 mb-2">
            Добро пожаловать в Medical API
        </h1>
        <p className="text-gray-600 max-w-md">
            Быстрая онлайн-запись к лучшим врачам города. Удобно. Просто. Надёжно.
        </p>
    </div>
);

export default HomePage;
