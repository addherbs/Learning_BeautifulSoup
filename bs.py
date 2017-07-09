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

print (soup.text)   # returns all the texts in the entire  page

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

get_url()
