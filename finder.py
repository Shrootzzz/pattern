from newspaper import Article
import newspaper

#this assmes that the articles we're parsing are all about gun violence 
def scrapeDB(url):
	gunText = []
	num = 0
	papers = newspaper.build(url, memoize_articles=False)	
	for paper in papers.articles:
		num+=1
		if num % 10 == 0:
			print(num)
		paper.download()
		paper.parse()
		print(paper.title)
		gunText.append(paper.text)
			
	return gunText

def scrapeNews(url):
	gunText = []
	num = 0
	papers = newspaper.build(url, memoize_articles=False)	
	for paper in papers.articles[0:200]:
		num+=1
		if num % 10 == 0:
			print(num)
		paper.download()
		paper.parse()
		paper.nlp()
		if ('gun' in paper.title) or ('shoot' in paper.title):
			if ('game' not in paper.keywords):
				print(paper.title)
				gunText.append(paper.text)
			
	return gunText