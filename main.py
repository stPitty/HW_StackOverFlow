import json
import requests
import time

class Dowloader:
    def __init__(self,params,id,path=''):
        self.params = params
        self.id = id
        self.path = path

# ---------------------------Скачивает указанную страницу, которую мы передали-------------------------------
    def dowload_from_stackoverflow_fixed_page(self,page):
        self.params['page'] = page
        url = f'https://api.stackexchange.com/2.3/{self.id}'
        headers = {'Content-Type': 'application/json'}
        with open(f'{self.path}{self.params["page"]}.json', 'w+') as file:
            responce = requests.get(url, params=self.params, headers=headers)
            json.dump(responce.json(), file, ensure_ascii=False, indent=2)
            return responce.json().get('has_more')

# ---------------------------Скачивает все страницы с данными по нашему запросу-------------------------------
    def dowload_from_stackoverflow_all_pages(self):
        page = 1
        while self.dowload_from_stackoverflow_fixed_page(page):
            page += 1

my_params = {'order': 'desc',
          'tagged': 'python',
          'site': 'stackoverflow',
          'fromdate': round(time.time()-2*24*60*60),
          'pagesize': '100',
          }

Download = Dowloader(my_params,'questions','files/')

Download.dowload_from_stackoverflow_fixed_page(4)
# Download.dowload_from_stackoverflow_all_pages()







