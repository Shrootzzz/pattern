from newspaper import Article, news_pool
import newspaper

print("Building and downloading your news sites...")
washington = newspaper.build('https://www.washingtonpost.com', memoize_articles=False)
nyp = newspaper.build('https://nypost.com/news/', memoize_articles=False)
google = newspaper.build('https://news.google.com', memoize_articles=False)
archive = newspaper.build('http://www.gunviolencearchive.org', memoize_articles=False)
foxnews = newspaper.build('http://www.foxnews.com', memoize_articles=False)
ex1 = Article('https://www.cnn.com/2017/12/14/us/sandy-hook-newtown-shooting-victims-profiles/index.html')
ex2 = Article('https://www.cbsnews.com/news/pulse-nightclub-shooting-orlando/')
ex3 = Article('https://www.nbcnews.com/news/us-news/beginning-era-1966-university-texas-clock-tower-shooting-n620556')
ex4 = Article('https://www.cnn.com/2016/09/28/us/south-carolina-elementary-school-shooting/index.html')
ex5 = Article('http://www.latimes.com/local/lanow/la-me-ln-norcal-elementary-school-shooting-20171114-story.html')
ex1.download()
ex2.download()
ex3.download()
ex4.download()
ex5.download()

papers = [washington, nyp, google, archive, foxnews]
news_pool.set(papers, threads_per_source=2)
news_pool.join()

size = 0
num = 0
data = []
articles = []

articles.append(ex1)
articles.append(ex2)
articles.append(ex3)
articles.append(ex4)
articles.append(ex5)
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

