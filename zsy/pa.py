#encoding:UTF-8
import re

from bs4 import BeautifulSoup
import lxml
import requests

with open ("C:/Users/dingdingche/Desktop/sy.txt","w",encoding="utf-8")as out:
    pass
with open("C:/Users/dingdingche/Desktop/error.txt", "w", encoding="utf-8") as error:
    pass

names=[]
with open("E:/Test/B10Kid_hal.tree.sorted")as f:
    lines=f.readlines()
    for line in lines:
        nn=line.split("\t")[2]
        names.append(nn)

for name in names:
    aname=name.replace("_","")
    findweb=f"https://avibase.bsc-eoc.org/search.jsp?qstr={name}"
    wb_data1 = requests.get(findweb)
    soup1 = BeautifulSoup(wb_data1.text, 'lxml')
    all_txt=soup1.prettify().replace("\n","").replace(" ","")
    links=re.findall(f"javascript:changespecies\(\'\w+\'\)\">{aname}<",all_txt)
    relinks=list(set(links))
    if len(relinks)!=1:
        synames = []
        try:
            parts=re.findall("avibaseid=\w+&sec=",all_txt)
            part=str(parts).split("=")[1]
            url=f'https://avibase.bsc-eoc.org/species.jsp?lang=EN&avibaseid={part}=synonyms'
            wb_data = requests.get(url)
            soup = BeautifulSoup(wb_data.text, 'lxml')

            for ch in soup.div.table.children:
                cch = str(ch).split("</td><td>")
                if cch:
                    if "\n" not in cch:
                        if "Avibase name" not in cch[0]:
                            synames.append(cch[1])
                            syname = ",".join(synames)
            with open("C:/Users/dingdingche/Desktop/sy.txt", "a", encoding="utf-8") as out:
                out.write(f"{name}\t{url}\t{syname}\n")
        except:
            with open ("C:/Users/dingdingche/Desktop/error.txt","a",encoding="utf-8") as error:
                error.write(f"{name}\t{len(relinks)}\t{findweb}\n")

    else:
        for link in relinks:
            synames=[]
            slink=link.split("'")[1]

            url = f'https://avibase.bsc-eoc.org/species.jsp?lang=EN&avibaseid={slink}&sec=synonyms'
            wb_data = requests.get(url)
            soup = BeautifulSoup(wb_data.text, 'lxml')

            for ch in soup.div.table.children:
                cch = str(ch).split("</td><td>")
                if cch:
                    if "\n" not in cch:
                        if "Avibase name" not in cch[0]:
                            synames.append(cch[1])
                            syname=",".join(synames)


        with open ("C:/Users/dingdingche/Desktop/sy.txt","a",encoding="utf-8")as out:
                out.write(f"{name}\t{url}\t{syname}\n")




'''
url = 'https://avibase.bsc-eoc.org/search.jsp?qstr=Tinamus_guttatus'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

for ch in soup.div.table.children:
    cch=str(ch).split("</td><td>")
    if cch:
        if "\n" not in cch :
            if "Avibase name" not in cch[0]:
                print(cch[1])

soup.findAll("td",text="Fringilla pecoris")

aa=soup.find_all("tr")
soup.find_all(sec="synonyms")
bb=soup.div.table.a.next_siblings
cc= soup.prettify()
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.next_siblings)
print(soup.p.attrs)
print(soup.p.string)
print(soup.div.attrs)
print(soup.div.tr.next_siblings)
print(soup.div.table.a.next_siblings)
'''