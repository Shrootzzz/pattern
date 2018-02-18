from newspaper import Article
import newspaper

def scrape(url):
	gunText = []
	num = 0
	cnn_papers = newspaper.build(url, memoize_articles=False)	
	for paper in cnn_papers.articles:
		num+=1
		if num % 10 == 0:
			print(num)
		paper.download()
		paper.parse()
		gunText.append(paper.text)
			
	return gunText