#encoding:UTF-8
import re

from bs4 import BeautifulSoup
import lxml
import requests
url = 'https://avibase.bsc-eoc.org/search.jsp?qstr=Tinamus_guttatus'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
cc = soup.prettify()