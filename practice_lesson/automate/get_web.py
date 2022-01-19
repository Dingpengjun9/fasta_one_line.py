#! python
#launches
import webbrowser,sys,pyperclip
if len(sys.argv)>1:
    address =" ".join(sys.argv[1:])
else:
    address=pyperclip.paste()
#address ="china shandong qingdao"
webbrowser.open("https://www.google.com/maps/place/"+address)

import requests
res =requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
with open("C:/Users/dingdingche/Desktop/romeo.txt","wb")as play_file:
    for chnk in res.iter_content(100000):
        play_file.write(chnk)

type(res)
res.status_code==requests.codes.ok
len(res.text)
print(res.text[:250])

import bs4,requests
res =requests.get('https://nostarch.com')
res.raise_for_status()
nostar=bs4.BeautifulSoup(res.text)
type(nostar)
element=nostar.select("div")
len(element)
type(element)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
browser=webdriver.Chrome("D:\Driver\chromedriver.exe")
type(browser)
browser.get("https://inventwithpython.com")
try:
    elem=browser.find_element(By.TAG_NAME,"div")
    print("11")
except:
    print("22")
link_elem=browser.find_element(By.LINK_TEXT,"Read for Free")
type(link_elem)
link_elem.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome("D:\Driver\chromedriver.exe")
browser.get("https://baidu.com/")
#email_element=browser.find_element()
user=browser.find_element(By.ID,"kw")
user.send_keys("sus")
user.submit()
html_element=browser.find_element(By.TAG_NAME,'html')
html_element.send_keys(Keys.END)
browser.back()
browser.forward()
browser.refresh()
browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome("D:\Driver\chromedriver.exe")
browser.get("https://www.ncbi.nlm.nih.gov/protein/")
find=browser.find_element(By.NAME,"term")
find.send_keys("(FGF8[Gene Name]) AND Taeniopygia_guttata[Organism] ")
find.submit()
error_names=browser.find_elements(By.TAG_NAME,"span")
err=browser.find_element(By.LINK_TEXT,"No items found.")
for i in error_names:
    if "No items found." in i.text:
        print(i.text)
reset=browser.find_element(By.CLASS_NAME,"reset")
reset.click()
fasta_b=browser.find_element(By.NAME,"EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.SequenceViewer.Sequence_ViewerTitle.ReportShortCut")
fasta_b.click()
fa_seq=browser.find_element(By.TAG_NAME,"pre")
print(fa_seq.text)

