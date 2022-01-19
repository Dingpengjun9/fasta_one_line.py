import re
from bs4 import BeautifulSoup
import lxml
import requests

with open("C:/Users/dingdingche/Desktop/error.txt",encoding="utf-8")as inf:
    lines=inf.readlines()
    for line in lines:
        synames = []
        name, url = line.split("\t")[0], line.split("\t")[2].rstrip("\n")
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')

        all_txt = soup.prettify().replace("\n", "")
        links = re.findall(f"javascript:changespecies\(\'\w+\'\)\">\s+\w+\s\w+\s+<", all_txt)
        relinks = list(set(links))

        for link in relinks:
            synames = []
            slink = link.split("'")[1]

            url = f'https://avibase.bsc-eoc.org/species.jsp?lang=EN&avibaseid={slink}&sec=synonyms'
            wb_data = requests.get(url)
            soup = BeautifulSoup(wb_data.text, 'lxml')

            for ch in soup.div.table.children:
                cch = str(ch).split("</td><td>")
                if cch:
                    if "\n" not in cch:
                        if "Avibase name" not in cch[0]:
                            synames.append(cch[1])
                            syname = ",".join(synames)
        with open ("C:/Users/dingdingche/Desktop/syy.txt","a",encoding="utf-8")as out:
                out.write(f"{name}\t{url}\t{syname}\n")