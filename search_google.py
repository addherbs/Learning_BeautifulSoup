from google import search


song_name = 'main+tera+hero'
prefix = 'https://www.google.com/search?q=lyricsmint.com+main+tera+hero'

#Not original results
#About 40 results per hour
## gives google results
def search_google():
    count = 0
    links = []
    for link in search('www.google.com'):
        count = count +1
		links.append(link)
        if count == 10:
            break
