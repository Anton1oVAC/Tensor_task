import requests
from datetime import datetime, timezone
import pytz

def request_to_the_server(url):
    try:
        response = requests.get(url)
        response.raise_for_status()    
        return response.json()
    # Ошбика юрл
    except requests.exceptions.MissingSchema:
        raise ValueError(f"Неверный URL: {url}")
    # Ошибка
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Ошибка запроса: {e}")

def main():  
    url = 'https://yandex.com/time/sync.json?geo=213'
    deltas = []

    for _ in range(5):
        start_time = datetime.now(timezone.utc)

        try:
            # вывод запроса
            data = request_to_the_server(url) 
            print('\n')
            print(f"Заспрос:\n", data)
    
            # преобразую время в секунды
            timestamp = data['time'] / 1000
            # время исходя из моей временной зоны
            local_time = datetime.fromtimestamp(timestamp, timezone.utc).astimezone()
            # получение названия временной зоны
            timezone_name = local_time.astimezone(pytz.timezone('Europe/Moscow')).tzname()
            print(f"Время запроса: {local_time.strftime('%Y-%m-%d %H:%M:%S')} ({timezone_name})")
    
            # Вычисление дельты времени на запрос
            end_time = datetime.now(timezone.utc)
            delta = (end_time - start_time).total_seconds()
            deltas.append(delta)
            print(f"Дельта: {delta:.6f}")
        
        except (ValueError, RuntimeError) as e:
            print(e)
            break
            
    # Вычисление средней дельты за 5 запросов
    if deltas:
        average_delta = sum(deltas) / len(deltas)
        print(f"\nСредняя дельта: {average_delta:.6f}")

   
if __name__ == '__main__':
    main()
