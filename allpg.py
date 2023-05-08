import requests
from bs4 import BeautifulSoup
url="https://www.astro.com/astro-databank/Special:AllPages"
r=requests.get(url)
soup=BeautifulSoup(r.text, "lxml").find("ul",{"class":"mw-allpages-chunk"}).find_all("a")

links=[]
for i in soup:
    links.append("https://www.astro.com"+i.get("href"))

# print(links)
