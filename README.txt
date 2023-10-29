# Для создания события (POST-запрос):
curl -X POST -d "2023-10-30|Заголовок события|Текст события" http://localhost:5000/api/v1/calendar/

# Для получения списка событий (GET-запрос):
curl http://localhost:5000/api/v1/calendar/

# Для чтения конкретного события (GET-запрос):
curl http://localhost:5000/api/v1/calendar/1/

# Для обновления события (PUT-запрос):
curl -X PUT -d "2023-10-30|Измененный заголовок|Измененный текст" http://localhost:5000/api/v1/calendar/1/

# Для удаления события (DELETE-запрос):
curl -X DELETE http://localhost:5000/api/v1/calendar/1/
