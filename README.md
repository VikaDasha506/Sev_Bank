Проект "Банк". Установка и запуск проекта

1. Клонировать проект командой: git clone https://github.com/VikaDasha506/Sev_Bank
2. Создайте виртуальное окружение внутри папки проекта: python -m venv venv
3. Активируйте виртуальное окружение: Для Windows в Command Prompt: venv\Scripts\activate Для Windows в PowerShell: .\venv\Scripts\Activate.ps1
4. Установите все зависимости проекта командой: pip install -r requirements.txt
5. Примените миграции для настройки структуры базы данных: python manage.py migrate
6. Загрузите данные в таблицу командой: python manage.py loaddata dump.json
7. Все пароли и ключи спрятаны в файл .env , так что Вам необходимо, предварительно создав файл (.env), записать в него свои данные. Вот пример: SECRET_KEY=ВВЕДИТЕ_ДЖАНГО_СЕКРЕТНЫЙ_КЛЮЧ EMAIL_HOST_PASSWORD=ВВЕДИТЕ_ПАРОЛЬ_ОТ_ПОЧТЫ EMAIL_HOST=ВВЕДИТЕ_ХОСТ_ПОЧТЫ EMAIL_PORT=ВВЕДИТЕ_ПОРТ_ПОЧТЫ EMAIL_HOST_USER=ВВЕДИТЕ_ВАШ_ЕМЕЙЛ TELEGRAM_BOT_TOKEN=ВАШ_ТОКЕН_БОТА YOUR_PERSONAL_CHAT_ID=ВАШ_ЧАТ_АЙДИ
8. Запустите встроенный сервер разработки командой: python manage.py runserver
9. Откройте веб-браузер и перейдите по адресу:  http://127.0.0.1:8000/ для доступа к вашему приложению
10. Доменное имя https://sev-bank.ru/