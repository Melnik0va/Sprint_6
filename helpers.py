
from datetime import datetime, timedelta
import random

#генерация даты доставки на следующий день с текущей даты
def generate_delivery_date():
    # Получаем текущую дату
    today = datetime.now()
    
    # Генерируем случайное время доставки на следующий день
    next_day = today + timedelta(days=1)
    
    # Форматируем дату в нужный формат
    return next_day.strftime('%d.%m.%Y')

#генерация случайного номера
def generate_random_phone():
	return '+7' + str(random.randint(1000000000, 9999999999))

