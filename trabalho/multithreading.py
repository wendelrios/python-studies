import requests
import json
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed

mensagem = input('digite a mensagem a ser enviada ao servidor: ')
payload = {'message': mensagem}

url_list = ['https://api.github.com/users/wendelrios']

def download_file(url, file_name):
    try:
        html = requests.get(url, stream=True, params=payload)
        print(html.content)
        open('{file_name}.json'.format(file_name=file_name), 'wb').write(html.content)
        return html.status_code
    except requests.exceptions.RequestException as e:
       return e

def runner():
    threads= []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for url in url_list:
            file_name = uuid.uuid1()
            threads.append(executor.submit(download_file, url, file_name))
           
        for task in as_completed(threads):
            print(task.result())
            
      
runner()




