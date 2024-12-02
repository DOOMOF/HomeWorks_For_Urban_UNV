import requests

# URL, к которому будет отправлен запрос
url = "https://jsonplaceholder.typicode.com/posts"

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем статус-код ответа
if response.status_code == 200:
    # Успешный запрос, выводим данные
    print("Данные, полученные с сайта:")
    print(response.json())  # выводим в формате JSON
else:
    # Если запрос не успешен, выводим сообщение об ошибке
    print(f"Ошибка {response.status_code}: не удалось получить данные.")