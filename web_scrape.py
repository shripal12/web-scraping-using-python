import urllib.request
import requests
from bs4 import BeautifulSoup
import os

def spider(max_pages):
    page = 1
    while page <= max_pages:
        dir_name = 'pix_' + str(page)
        print("page "+str(page)+ " started")
        os.mkdir(dir_name, mode=0o777)
        url = r'https://thenewboston.com/search.php?type=0&sort=reputation&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        imglink = soup.select('tr > td[class$="valign-top"] > a > img')
        names = soup.select('tr > td > div > a[class="user-name"]')
        for i in range(len(names)):
            try:
                filename = names[i].string.strip() + '.jpg'
                image=imglink[i].get('src')
                urllib.request.urlretrieve(r'https://thenewboston.com'+image, filename)
                os.rename(filename, r'pix_'+str(page)+r'/'+filename)
            except OSError as e:
                print ("skipped an iteration: " + format(e))
                continue
        print("page "+str(page)+ " over")
        page += 1

# As an argument to spider function, enter THE NUMBER OF PAGES you want to scrape, starting from 1, from www.thenewboston.com users' list.
spider(2)
