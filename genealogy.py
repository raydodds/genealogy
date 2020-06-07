"""	geneaology.py
	Reads in the spreadsheet of house genealogy in order
"""

import member

import graphviz

import argparse

DEFAULT_FILE_NAME='relations'

def main():
	

	parser = argparse.ArgumentParser()
	parser.add_argument("member_list",
						help="A tsv file pulled from the EHouse Genealogy")
	parser.add_argument("-o","--out_file",
						help="The output filename (will have .pdf appended)",
						default=DEFAULT_FILE_NAME)
	parser.add_argument("-q", "--quiet", action='store_true',
						help="Does not print a list of unconnected members")

	args = parser.parse_args()
	"""
	if(len(sys.argv) != 2):
		usage()
		exit()
	"""	

	readFile = ""
	try:
		readFile = open(args.member_list, 'r+')
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

	graph.attr(label="""<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
	<TR><TD COLSPAN="3" BORDER="1"><B>Engineering House Lines</B></TD></TR>
	<TR><TD ALIGN="left">Dashed Line</TD><TD>--&gt;</TD><TD ALIGN="right">Adoption</TD></TR>
	<TR><TD ALIGN="left">Blue Outline</TD><TD>--&gt;</TD><TD ALIGN="right">EBoard</TD></TR>
	<TR><TD ALIGN="left">Yellow Outline</TD><TD>--&gt;</TD><TD ALIGN="right">Cabinet</TD></TR>
</TABLE>>""")
	graph.attr(labeljust='l')
	graph.attr(labelloc='t')

	if not args.quiet:
		print("Unconnected members:")

	for mem in roster:
		if roster[mem].isConnected():
			if(roster[mem].isEBoard()):
				graph.node(mem, mem, color='blue')
			elif(roster[mem].isCabinet()):
				graph.node(mem, mem, color='gold')
			else:
				graph.node(mem, mem)

			if(len(roster[mem].mentees) == 0):# and len(roster[mem].adoptees) == 0):
				graph.node(mem, mem, shape='egg')

			
			for mentee in roster[mem].mentees:
				graph.edge(mem, mentee.name)

			for adoptee in roster[mem].adoptees:
				graph.edge(mem, adoptee.name, style='dashed')
		elif not args.quiet:
			print(f'{roster[mem].name}')

	graph.render(args.out_file)
		
"""
def usage():
	print("python3 genealogy.py <filename>")

"""



if __name__ == "__main__":
	main()
