import bs4 as bs
import urllib.request

source = urblib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(source,'lxml')