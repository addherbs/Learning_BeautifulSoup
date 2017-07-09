import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request

source = urllib.request.urlopen ('https://pythonprogramming.net/parsememcparseface/').read ()
soup = BeautifulSoup(source, 'lxml')

# Understanding title
def get_title():
    title_with_tag = soup.title
    title_name = soup.title.name
    title_main = soup.title.string  # title_main = soup.title.text

# print (soup.text)   # returns all the texts in the entire  page

# Understanding P tag
def get_p():
    first_p = soup.p
    all_p = soup.find_all ('p')
    for para in soup.find_all ('p'):
        print (para)    #returns everthing with tags
        print ('----------------')
        print (para.string) #only returns main string if there are no inner tags
        print ('----------------')
        print (para.text)   #returns the entire main string .. irrespective of the inner tags
        print ('\n--------xxxxxxxxx-----')

def get_url():
    for url in soup.find_all('a'):
        print(url.get('href'))

def get_specific():
    for div in soup.find_all('div',class_='body'):
        print(div.text)

# get_specific()
# print(soup.text)

def parse_table():
    table = soup.table  #soup.find('table')
    # print(table)
    allrows =   table.find_all('tr')
    for tr in allrows:
        td = tr.find_all('td')
        row = [each.text for each in td]
        print(row)

parse_table()
