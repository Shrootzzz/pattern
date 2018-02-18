from finder import scrapeDB, scrapeNews
# cnn = 'http://cnn.com'
# cnnUrl = scrape(cnn, num)
# print(cnnUrl)

google = 'https://news.google.com'
googleUrl = scrapeNews(google)
	
url = 'http://www.gunviolencearchive.org'
data = scrapeDB(url)

data.extend(googleUrl)

with open('article_url.txt', 'w', encoding='utf-8') as f:
	for article in data:
		f.write(article)