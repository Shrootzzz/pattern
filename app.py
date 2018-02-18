import re

templates = ["[a-z|A-Z|0-9|\,|\-]*\swas shot[a-z|A-Z|\s|0-9|\,|\-|]*in\s[a-z|A-Z|0-9|\,|\-]*"]
holderlist = []
segments = []
name = []
place = []
filename = "data.txt"

myFile = open(filename,"r")

text = myFile.read()

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

for i in range(0,10):
	for template in templates:
		print
		results = re.findall(template,str(text))
		if results:
			for result in results:
				# print(template)
				segments.append(result)
				myPattern = result
				myWords = myPattern.split(" ")
				myNewPattern = ""
				counter = 0
				for word in myWords:
					# print(myWords)	
					if (counter==0):
						myNewPattern+="[a-z|A-Z|0-9|\,|\-|]*\s"
						name.append(word)
					elif (counter==len(myWords)-1):
						myNewPattern+="\s[a-z|A-Z|0-9|\,|\-|]*"
						place.append(word)
					else:
						myNewPattern+=word
					counter+=1
				holderlist.append(myNewPattern)
	templates.extend(holderlist)
	templates = Remove(templates)
	name = Remove(name)
	place = Remove(place)
	holderlist = []

print(templates)
print(name)
print(place)

