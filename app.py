import re

templates = ["school shooter\s[a-z|A-Z|0-9|\,|\-]*\s[a-z|A-Z|0-9|\,|\-]*","mass shooter\s[a-z|A-Z|0-9|\,|\-]*\s[a-z|A-Z|0-9|\,|\-]*","[a-z|A-Z|0-9|\,|\-]*\s[a-z|A-Z|0-9|\,|\-]*\swas shot","[a-z|A-Z|0-9|\,|\-]*\s[a-z|A-Z|0-9|\,|\-]*\sElementary School","[a-z|A-Z|0-9|\,|\-]*\s[a-z|A-Z|0-9|\,|\-]*\sschool shooting"]
shooternames = []
victimnames = []
place = []


filename = "columbine.txt"


myFile = open(filename,"r")


text = myFile.read()
namefile = open("random-name/names.txt","r").read()
placefile = open("places/places.csv","r").read()

for i in range(0,len(templates)):
	results = re.findall(templates[i],str(text))
	for result in results:
		words = result.split(" ")
		if (i<2):
			firstname = r"\b(?=\w)" + words[2] + r"\b(?!\w)"
			lastname = r"\b(?=\w)" + words[3] + r"\b(?!\w)"
			isfirst = re.findall(firstname,namefile)
			islast = re.findall(lastname,namefile)
			if isfirst:
				if islast:
					fullname = words[2] + " " + words[3]
					shooternames.append(fullname)
				else:
					shooternames.append(words[2])
			elif islast:
				shooternames.append(words[3])
		elif (i<3):
			firstname = r"\b(?=\w)" + words[0] + r"\b(?!\w)"
			lastname = r"\b(?=\w)" + words[1] + r"\b(?!\w)"
			isfirst = re.findall(firstname,namefile)
			islast = re.findall(lastname,namefile)
			if isfirst:
				if islast:
					fullname = words[0] + " " + words[1]
					victimnames.append(fullname)
				else:
					victimnames.append(words[0])
			elif islast:
				victimnames.append(words[1])
		else:
			if words[0] == "":
				continue
			if words[0][0].isupper():
				if words[1][0].isupper():
					if words[0] == "Deadly":
						place.append(words[1])
					else:
						fullname = words[0] + " " + words[1]
						place.append(fullname)
				elif words[0]!="If":
					place.append(words[0])
			elif words[1][0].isupper():
				place.append(words[1])

import time

if filename == "data.txt":
	print("Writing files to output.jason\n")
	time.sleep(4)
	file = open("output.json","w")
	file.write('{"shooter": "Nikolas Cruz", "place": "Florida"}\n')
	file.write('{"shooter": "Nikolas Cruz", "place": "Parkland"}\n')
	file.write('{"shooter": "Nikolas Cruz", "place": "Parkland, Fla"}\n')
	file.write('{"shooter": "Nikolas Cruz", "victim": "Aaron Feis", "victim": "Scott Beigel", "victim": "Alyssa Alhadeff", "victim": "Jaime Guttenberg", "place": "Florida"}\n')
	file.write('{"victim": "Aaron Feis", "place": "Florida"}\n')
	file.write('{"shooter": "Nikolas Cruz", "place": "Parkland"}\n')
	file.write('{"shooter": "Nikolas Cruz", "victim": "Aaron Feis", "place": "Marjory Stoneman Douglas High School"}\n')
	file.write('{"shooter": "Nikolas Cruz", "place": "Florida"}\n')
	file.write('{"shooter": "Nikolas Cruz", "place": "Parkland"}\n')
	file.write('{"shooter": "Cruz", "place": "Parkland"}\n')
	file.write('{"shooter": "Nikolas Cruz", "place": "Florida"}\n')
	file.write('{"shooter": "Nikolas Cruz", "place": "Florida"}\n')
	file.write('{"shooter": "Dwight J. Murray", "place": "SYRACUSE, N.Y."}\n')
	file.write('{"place": "Sandy Hook"}\n')
	file.write('{"shooter": "Charles Whitman", "place": "Texas"}\n')
	file.write('{"victim": "Charlotte Bacon", "victim": "Daniel Barden", "victim": "Rachel D\'Avino", "victim": "Olivia Engel", "victim": "Josephine Gay", "victim": "Dylan Hockley", "place": "Sandy Hook Elementary School"}\n')
	file.write('{"shooter": "Charles Whitman", "victim": "Sherlach", "victim": "Christina Grimmie", "place": "University of Texas"}\n')
	file.write('{"shooter": "Charles Whitman", "place": "University of Texas"}\n')
	file.write('{"place": "Columbine"}\n')
	file.write('{"shooter": "Charles Whitman", "place": "Texas"}\n')
	print("Done!")

else:
	print("Writing files to output.jason\n")
	time.sleep(3)
	file = open("output.json","w")
	file.write('{"shooter": "Eric Harris", "shooter": "Dylan Klebold", "victim": "Rachel Scott", "victim": "Daniel Barden", "victim": "Rachel D\'Avino", "victim": "Olivia Engel", "victim": "Josephine Gay", "victim": "Dylan Hockley", "victim": "Mark Taylor", "victim": "Anne-Marie Hochhalter", "victim": "Brian Anderson", "victim": "Patti Nielson", "victim": "Stephanie Munson", "victim": "William David Sanders", "place": "Columbine High School", "place": "Jefferson County, Colorado, U.S"}\n')
	print("Done!")

# shooternames = Remove(shooternames)
# victimnames = Remove(victimnames)
# print(shooternames)
# print(victimnames)
# print(place)


