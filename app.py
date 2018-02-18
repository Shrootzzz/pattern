import re

templates = []
segments = []
filename = "article_url.txt"

pattern = re.compile("[a-z|A-Z|0-9|\,|\-|]*\swoman\s+[a-z|A-Z|\s|0-9|\,|\-|]*\s*was killed\s[a-z|A-Z|0-9|\,|\-|]*")
#\s+[a-z|A-Z|\s|0-9|\,|\-]+\s+

myFile = open(filename,"r")

text = myFile.read()
sentences = text.split(".")

for sentence in sentences:
	result = re.search(pattern,str(sentence))
	if result:
		myPattern = result.group(0)
		