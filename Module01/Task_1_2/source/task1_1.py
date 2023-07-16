# Работают только первые три запроса на ссылки новых страниц, далее, видимо, сайт hh.ru блокирует запросы.
import time
from requests_tor  import RequestsTor
from bs4 import BeautifulSoup
import json
import tqdm
data = {
    "data":[]
}
req = RequestsTor()

i=0
for page in range(1,40):
  url = "https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=100&page={page}2&hhtmFrom=vacancy_search_list"
  resp = req.get(url)
  soup = BeautifulSoup(resp.text, "lxml")
  tags = soup.find_all(attrs={"class":"serp-item__title"})
  tag_price = soup.find_all(attrs={"class":"vacancy-serp-item-body__main-info"})
  for iter in tqdm.tqdm(tags):
    time.sleep(4)
    url_object =  iter.attrs["href"]
    tag_region = soup.find_all(attrs={"data-qa":"vacancy-serp__vacancy-address"})[i].text
    resp_object = req.get(url_object)
    soup_object = BeautifulSoup(resp_object.text, "lxml")
    tag_price = soup_object.find_all(attrs={"data-qa":"vacancy-salary"})[0].text
    tag_skill = soup_object.find_all(attrs={"class":"vacancy-description-list-item"})
    tag_skill = soup_object.find_all(attrs={"data-qa":"vacancy-experience"})[0].text
    print(iter.text, tag_skill, tag_price,  tag_region)
    i=+1
    data["data"].append({"title":iter.text, "work exprience":tag_skill,"salary":tag_price, "region":tag_region})
    with open("data.json", "w", encoding = 'UTF-8') as file:
      json.dump(data,file, ensure_ascii=False)
#print(tags)        

  