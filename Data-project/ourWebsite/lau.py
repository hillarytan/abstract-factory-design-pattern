from django.db import models
from bs4 import BeautifulSoup
import requests
url = "https://www.lau.edu.lb/fees/2022-2023/"
result = requests.get(url)
laumajor = list()
lauprice = list()
doc = BeautifulSoup(result.text, "html.parser")
tbody = doc.find_all("tbody")
trs1 = tbody[0].contents

x = len(trs1)
for i in range(x-1):
    if (i == 25) or (i == 73) or (i == 1):
        first = trs1[i].contents
        firstmaj = first[1].text
        firstmajsplitted = firstmaj[5:]
        firstprice = first[7].text
        firstpricesplitted = firstprice[5:]
        laumajor.append(firstmajsplitted)
        lauprice.append(firstpricesplitted)

    else:
        if (i % 2 == 1):

            tds = trs1[i].contents
            maj = tds[1].text
            major = maj[1:]
            p = tds[7].text
            price = p[5:]
            laumajor.append(major)
            lauprice.append(price)


class listLAU(models.Model):
    def laumajor():
        return laumajor

    def lautf():
        return lauprice
