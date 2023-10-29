Запуск файлом server.py из папки calendar

----------------------------


# Для создания события (POST-запрос):
curl http://localhost:5000/api/v1/calendar/ -X POST -d "2023-10-30|Заголовок события|Текст события"

# Для получения списка событий (GET-запрос):
curl http://localhost:5000/api/v1/calendar/

# Для чтения конкретного события (GET-запрос):
curl http://localhost:5000/api/v1/calendar/1/

# Для обновления события (PUT-запрос):
curl http://localhost:5000/api/v1/calendar/1/ -X PUT -d "2023-10-30|Измененный заголовок|Измененный текст"

# Для удаления события (DELETE-запрос):
curl http://localhost:5000/api/v1/calendar/1/ -X DELETE
