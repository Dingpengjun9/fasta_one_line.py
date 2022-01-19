#encoding:UTF-8
import re

from bs4 import BeautifulSoup
import lxml
import requests
bbb=[]
with open("C:/Users/dingdingche/Desktop/1.txt")as ff:
    fflines=ff.readlines()
    for filne in fflines:
        bbname=filne.strip("\n")
        bbb.append(bbname)

names=[]
ccname={}
with open("E:/beak/Synonym.txt")as f:
    lines=f.readlines()
    for line in lines:

        tname,nn=line.split("\t")[0],line.split("\t")[1].strip("\n")
        if tname in bbb:
            ccname[tname]=nn.replace(" ","-").split(",")
a=[]
b=[]
c=[]
for k in ccname.keys():
    for name in ccname[k]:

        findweb = f"https://www.phenome10k.org/{name}"
        wb_data = requests.get(findweb)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        cc = soup.prettify()
        if "3D / Web GL" in cc:
            a.append(name)
            print(k)
        elif "Sorry, the page you're looking for doesn't exist" in cc:
            b.append(name)
        else:
            c.append(name)

with open("C:/Users/dingdingche/Desktop/1.txt","w")as out:
    for aa in a:
        out.write(f"{aa}\n")














for name in names:
    aname=name.replace("_","")
    findweb=f"https://avibase.bsc-eoc.org/search.jsp?qstr={name}"
    wb_data1 = requests.get(findweb)
    soup1 = BeautifulSoup(wb_data1.text, 'lxml')
    all_txt=soup1.prettify().replace("\n","").replace(" ","")
    links=re.findall(f"javascript:changespecies\(\'\w+\'\)\">{aname}<",all_txt)
    relinks=list(set(links))
    if len(relinks)!=1:
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





url = 'https://www.phenome10k.org/Apteryx-rowi'

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
print(cc)
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