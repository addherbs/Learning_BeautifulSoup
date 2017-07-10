from google import search

## gives google results
def search_google():
    count = 0
    links = []
    for link in search('www.google.com'):
        links.append(link)
        count = count +1
        if count == 10:
            break
