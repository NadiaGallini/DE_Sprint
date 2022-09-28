from random import randint
from time import sleep
from requests import get as requests_get
from bs4 import BeautifulSoup
import json

data = {
    
    "data":[]
}

def headers():
    headers = dict()
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    return headers

for page in range(1,200):
        print(page)
        p_url = f"https://hh.ru/search/vacancy?text=python+разработчик&from=suggest_post&area=1&page={page}&hhtmFrom=vacancy_search_list"
        resp = requests_get(p_url, headers=headers())
        soup = BeautifulSoup(resp.text, "lxml")
        tags = soup.find_all(class_="vacancy-serp-item-body")
        # print(tags)
        if len(tags)==0:
            break
                
        for iter in tags:
            sleep(randint(1, 3))  
            tag_title = iter.find(attrs={"data-qa": "serp-item__title"})
                                   
            link_resp = requests_get(tag_title.attrs['href'], headers=headers())
            soup_item = BeautifulSoup(link_resp.text, "lxml")    
            
            tag_region = soup_item.find(attrs={"data-qa": "vacancy-serp__vacancy-address"}) 
                       
            tag_salary = soup_item.find(attrs={"data-qa": "vacancy-salary"}) 
                                   
            tag_worke = soup_item.find(attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"}) 
                                     
            data["data"].append({"title":iter.text, "work experience":tag_worke and tag_worke.text,  "salary":tag_salary and tag_salary.text, "region":tag_region and tag_region.text})
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)