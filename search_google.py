from google import search


song_name = 'main+tera+hero'
prefix = 'https://www.google.com/search?q=lyricsmint.com+main+tera+hero'
## gives google results
def search_google():
    count = 0
    links = []
    for link in search('www.google.com'):
        links.append(link)
        count = count +1
        if count == 10:
            break
