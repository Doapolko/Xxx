import requests
import re

def check_breaches(email):
    # Использование API HaveIBeenPwned (легальная проверка утечек)
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": "ВАШ_КЛЮЧ_API"}  # Требуется регистрация
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else []

def get_ip_info(ip):
    # Геолокация IP через сервис ipapi (легально для своих IP)
    data = requests.get(f"https://ipapi.co/{ip}/json/").json()
    return {k: data.get(k) for k in ['city', 'region', 'country_name', 'org']}

# Пример использования (только для своих данных!):
print(check_breaches("ВАШ_EMAIL@example.com"))  # Проверка своих утечек
print(get_ip_info("8.8.8.8"))  # Публичный IP Google DNS
