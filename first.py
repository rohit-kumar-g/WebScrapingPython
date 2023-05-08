print("Satyam is great and rohit is little more great")
import requests
from bs4 import BeautifulSoup
import pandas as pd
import allpg as ap
# url="https://www.astro.com/astro-databank/Abel,_Ren%C3%A9e"
links=ap.links

name=[]
gender=[]
time=[]
place=[]
tz=[]
rr=[]
cat=[]



# print(soup)
# tablee=soup.find("table",{"class":"infobox"}).find_all("tr")
ii=0
df = pd.DataFrame(columns=["name","gender","time",'place','timezone','Rodden Rating','Category'])
for i in links[0:11]:
  url=i
  print(ii)
  ii=ii+1
  try:
  

    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    tablee=soup.find("table",{"class":"infobox"})
    if tablee == None:
      continue
    namee= tablee.find(string="Name").find_next("td").text.split("Gender: ")[0] if (tablee.find(string="Name")!=None) else "null"
    genderr=tablee.find(string="Name").find_next("td").text.split("Gender: ")[1] if (tablee.find(string="Name")!=None) else "null"
    timee= "null" if (tablee.find(string="born on")==None) else tablee.find(string="born on").find_next("td").text
    placee=  "null" if(tablee.find(string="Place")==None) else tablee.find(string="Place").find_next("td").text
    tzz=  tablee.find(string="Timezone").find_next("td").text if (tablee.find(string="Timezone")!=None) else "null"
    rrr= "null" if(tablee.find(string="Rodden Rating")==None) else tablee.find(string="Rodden Rating").find_next("b").text
    # genderr=tablee.find(string="Gender").parent.parent.text
    cattList = [] if(soup.find("div",{"class":"mw-normal-catlinks"})==None) else soup.find("div",{"class":"mw-normal-catlinks"}).find_all("li")
    soup.decompose()
    catt=[]
    cato=""
    for i in cattList:
      catt.append(i.text)
      cato="&".join(catt)
    name.append(namee)
    gender.append(genderr)
    time.append(timee)
    place.append(placee)
    tz.append(tzz)
    rr.append(rrr)
    cat.append(cato)
    df.loc[ii] =[ namee.strip(), genderr.strip(), timee.strip(), placee.strip(), tzz.strip(), rrr.strip(), cato.strip()]
    print(df)
  except Exception as e:
    print(e)
    continue
    # print("except",ii)
    # df.to_csv("inal_satyam_ius_great_databutRohitIsMore.csv")
    # df.to_pickle("kuch.pkl")

  

# print(tablee,len(tablee))
# print(tablee.find(string="Nameftdgt"))



# ull=soup.find("ul",{"class":"mw-allpages-chunk"})
# print(name)
# df=pd.DataFrame({"name":name,"gender":gender,"time":time,"place":place,"timezone":tz,"Rodden Rating":rr,"Category":cat})
# df.to_pickle("kuch.pkl")
# df.to_csv("inal_satyam_ius_great_databutRohitIsMore.csv")

# titles=[]
# links=[]


# print(links)

df.to_csv("final_satyam_is_great_databutRohitIsMore.csv")
df.to_pickle("kuch.pkl")

