from newspaper import Article, news_pool
import newspaper

print("Building and downloading your news sites...")
washington = newspaper.build('https://www.washingtonpost.com', memoize_articles=False)
nyp = newspaper.build('https://nypost.com/news/', memoize_articles=False)
google = newspaper.build('https://news.google.com', memoize_articles=False)
archive = newspaper.build('http://www.gunviolencearchive.org', memoize_articles=False)
foxnews = newspaper.build('http://www.foxnews.com', memoize_articles=False)

papers = [washington, nyp, google, archive, foxnews]
news_pool.set(papers, threads_per_source=2)
news_pool.join()

size = 0
num = 0
data = []
articles = []

articles.extend(washington.articles)
articles.extend(nyp.articles)
articles.extend(google.articles)
articles.extend(google.articles)

print("Parsing the articles...")
for paper in articles:
	num+=1
	paper.parse()
	if num % 10 == 0:
		print(num)
	if ('gun' in paper.title) or ('shoot' in paper.title) or ('Gun' in paper.title) or ('Shoot' in paper.title):
		paper.nlp()
		if ('game' not in paper.keywords):
			size +=1
			print(paper.title)
			data.extend(paper.text)

print(str(size) + " articles")

print('Writing into text file...')
with open('data.txt', 'w', encoding='utf-8') as f:
	for article in data:
		f.write(article)

