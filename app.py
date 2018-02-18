import wikipedia
import re

pages = wikipedia.search("shooting")
print(pages)
i=0

pattern = re.compile("\s+[a-z|A-Z|\s]+\s+shot\s+[a-z|A-Z|\s]+\s+")
# group = pattern.match(") is an American politician who ")
# print(group)

for page in pages:
	if "disambiguation" in page:
		continue
	myGroup = pattern.search(wikipedia.page(page).content)
	print(page)
	print(myGroup)
		