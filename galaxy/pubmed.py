import requests
import re
import sys
key=sys.argv[1]                #input("查找信息：")
num=sys.argv[2]
out_file=sys.argv[3]
#local_url=input("储存目录")
turl="https://pubmed.ncbi.nlm.nih.gov/"
tdata=requests.get(turl,params={"term":key}).text
pat_allpage='<span class="total-pages">(.*?)</span>'
allpage=re.compile(pat_allpage,re.S).findall(tdata)
if int(num) > int(str(int(allpage[0].replace('\n        ','').replace(',',''))*10)):
    num=int(str(int(allpage[0].replace('\n        ','').replace(',',''))*10))
with open("pubmed.html","a",encoding="utf-8")as out:
    pass
for j in range(0,int(num)//10+1):
    url="https://pubmed.ncbi.nlm.nih.gov/"+"?term="+key+"&page="+str(j+1)
    data=requests.get(url,params={"term":key}).text
    pat1_content_url='<div class="docsum-wrap">.*?<.*?href="(.*?)".*?</a>'
    content_url=re.compile(pat1_content_url,re.S).findall(data)
    hd={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
    for i in range(0,len(content_url)):
        curl="https://pubmed.ncbi.nlm.nih.gov/"+content_url[i]
        try:
            cdata=requests.get(curl,headers=hd).text
            pat2_title="<title>(.*?)</title>"
            pat3_content='<div class="abstract-content selected".*?>(.*?)</div>'
            pat4_date='<span class="cit">(.*?)</span>'
            title=re.compile(pat2_title,re.S).findall(cdata)
            print("正在获取："+title[0])
            content=re.compile(pat3_content,re.S).findall(cdata)
            date=re.compile(pat4_date,re.S).findall(cdata)
            fh=open(out_file,"a",encoding="utf-8")
            abs=str(content[0]).split("<")[1].split(">")[1].replace("\n","").strip(" ")
            fh.write(str(title[0])+' ----'+str(date[0])+"\n"+abs+"\n")
            fh.close
        except Exception as err:
            pass
        if int(num) < 10:
            if i+1 == int(num):
                break
        elif int(num) == 10:
            if i == 9:
                break
        elif (j*10)+i+1 == int(num):
            break