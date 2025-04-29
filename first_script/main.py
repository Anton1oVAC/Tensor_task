import requests
from datetime import datetime, timezone
import pytz

def request_to_the_server():
    url = 'https://yandex.com/time/sync.json?geo=213'
    response = requests.get(url)
    return response.json()

def main():
    
	for _ in range(5):
            
		#start_time = datetime.now(timezone.utc)
                
		# вывод запроса
		data = request_to_the_server()
		print('\n')
		print(f"Заспрос:\n", data)
		#print(f"Время начальное:", start_time.strftime('%Y-%m-%d %H:%M:%S'))
        
		# преобразую время в секунды
		timestamp = data['time'] / 1000
        # время исходя из моей временной зоны
		local_time = datetime.fromtimestamp(timestamp, timezone.utc).astimezone()
		# получение названия временной зоны
		timezone_name = local_time.astimezone(pytz.timezone('Europe/Moscow')).tzname()
		print(f"Время начальное:, {local_time.strftime('%Y-%m-%d %H:%M:%S')} ({timezone_name})")

            


   
if __name__ == '__main__':
    main()
