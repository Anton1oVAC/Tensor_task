import requests

def request_to_the_server():
    url = 'https://yandex.com/time/sync.json?geo=213'
    response = requests.get(url)
    return response.json()

def main():
    
    data = request_to_the_server()
    print(f"Заспрос:", data)
   
if __name__ == '__main__':
    main()
