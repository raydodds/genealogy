"""	geneaology.py
	Reads in the spreadsheet of house genealogy in order
"""

import graphviz, member, sys

def main():
	
	if(len(sys.argv) != 2):
		usage()
		exit()
		
	readFile = ""
	try:
		readFile = open(sys.argv[1], 'r+')
	except FileNotFoundError as e:
		print("File does not exist, try again asshole.")
		exit()

	roster = {}
	lines = []

# ['Last Name', 'First Name', 'Nickname', 'Mentee(Formatted)', 'Name of Mentor(s)', 'Adopted Mentor(s)', 'Positions', '\n']

	lineNum = 0
	for line in readFile:
		if(lineNum != 0):
			readLine = line.split('\t')
			lines += [readLine]

			attrib = ''
			attribs = readLine[6].strip().split(',')
			for attr in attribs:
				attrib += member.strToAttr(attr.strip())

			newMem = member.Member(readLine[3], attrib, readLine[2])
			roster[newMem.name] = newMem

		lineNum += 1

	for line in lines:
		name = line[3]
		mentors = line[4].split(',')
		adoptors = line[5].split(',')
		for mentor in mentors:
			if(mentor != ''):
				roster[name].addMentor(roster[mentor.strip()])

		for adoptor in adoptors:
			if(adoptor != ''):
				roster[name].addAdoptor(roster[adoptor.strip()])

	graph = graphviz.Digraph("Relations", format='pdf')

	for mem in roster:
		if(roster[mem].isEBoard()):
			graph.node(mem, mem, color='blue')
		elif(roster[mem].isCabinet()):
			graph.node(mem, mem, color='gold')
		else:
			graph.node(mem, mem)


		for mentee in roster[mem].mentees:
			graph.edge(mem, mentee.name)

		for adoptee in roster[mem].adoptees:
			graph.edge(mem, adoptee.name, style='dashed')

	graph.render('relations')
		

def usage():
	print("python3 genealogy.py <filename>")





if __name__ == "__main__":
	main()
