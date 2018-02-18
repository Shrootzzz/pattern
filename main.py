from finder import scrape
import io
# cnn = 'http://cnn.com'
# cnnUrl = scrape(cnn, num)
# print(cnnUrl)

# google = 'https://news.google.com'
# googleUrl = scrape(google, num)
# print(googleUrl)
	
url = 'http://www.gunviolencearchive.org'
data = scrape(url)

with io.open('article_url.txt', 'w', encoding='utf-8') as f:
	for article in data:
		f.write(article)