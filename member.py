""" member.py
	A class for describing the relations and attributes of a member of Engineering House
"""

class Member:

#
#	CLASS VARIABLES/CONSTANTS
#
	__slots__ = "name", "nicknames", "mentors", "mentees", "adoptors", "adoptees", "attributes"

	validAttributes = "oOPVSTAmnrhjbsfR"

#
#	SETUP AND BREAKDOWN
#
	def __init__(self, name, attributes="", nicknames=''):
		""" Initialization of the new member.
		"""
		self.name = name
		self.nicknames = nicknames
		self.mentors = []
		self.mentees = []
		self.adoptors = []
		self.adoptees = []
		if(type(attributes) == str):
			for char in attributes:
				if char not in Member.validAttributes:
					raise ValueError("only characters in " + Member.validAttributes + " are permitted")
			self.attributes = '' + attributes
		else:
			raise TypeError("attributes must be a string")

	def __str__(self):
		""" Returns the name as the string representation
		"""
		return self.name

	def __repr__(self):
		""" Returns a repr of the object without connections
		#"""
		return "("+self.name+", "+self.attributes+")"

#
#	ATTRIBUTE INTERACTION
#
	def setAttribute(self, attribute):
		""" adds an attribute to the attribute string
			@param: attribute[str] - the attribute to add
		"""
		if( type(attribute) is not str or len(attribute) > 1 ):
			raise TypeError("attributes must be a single character")
		else:
			if( attribute not in self.attributes and attribute in Member.validAttributes ):
				self.attributes += attribute

	def hasOneOf(self, checkAttributes):
		""" checks if the member has any of the given attributes
			@param checkAttributes[str] - the attributes to check
		"""
		for attr in checkAttributes:
			if( attr in self.attributes ):
				return True
		return False
	
	def isEBoard(self):
		# P : President
		# V : Vice President
		# S : Secretary
		# T : Treasurer
		return self.hasOneOf('PVST')
	
	def isCabinet(self):
		# A : ALC
		# m : Computer Head
		# n : Constitution/Historian
		# r : Recruitment Head
		# h : House Improvements Head
		# j : Project Head
		# b : Public Representative
		# s : Social Head
		# f : Freshman Rep
		return self.hasOneOf('Amnrhjbsf')

	def isOffFloor(self):
		# o : Off Floor
		return self.hasOneOf('o')

	def isRA(self):
		# R : RA
		return self.hasOneOf('R')

#
#	LINK INTERACTION
#

	def addMentor(self, member, _initialCall = True):
		if( self == member ):
			raise Exception("Member cannot be self-related.")

		if(member not in self.mentors):
			self.mentors.append(member)
		
		if(_initialCall):
			member.addMentee(self, False)
	
	def addMentee(self, member, _initialCall = True):
		if( self == member ):
			raise Exception("Member cannot be self-related.")

		if(member not in self.mentees):
			self.mentees.append(member)
		
		if(_initialCall):
			member.addMentor(self, False)
	
	def addAdoptor(self, member, _initialCall = True):
		if( self == member ):
			raise Exception("Member cannot be self-related.")	
		
		if(member not in self.adoptors):
			self.adoptors.append(member)
		
		if(_initialCall):
			member.addAdoptee(self, False)
	
	def addAdoptee(self, member, _initialCall = True):
		if( self == member ):
			raise Exception("Member cannot be self-related.")

		if(member not in self.adoptees):
			self.adoptees.append(member)
		
		if(_initialCall):
			member.addAdoptor(self, False)

	def isConnected(self):
		if sum(map(lambda x: len(x), [self.mentees, self.mentors, self.adoptees, self.adoptors])) == 0:
			return False
		return True


#
#	Class Methods
#

def strToAttr(string):
	# P : President
	# V : Vice President
	# S : Secretary
	# T : Treasurer
	# A : ALC
	# m : Computer Head
	# n : Constitution/Historian
	# r : Recruitment Head
	# h : House Improvements Head
	# j : Project Head
	# b : Public Representative
	# s : Social Head
	# f : Freshman Rep
	# o : Off-Floor
	# R : RA
	# O : Off-Floor Rep
	
	if(string == "President"):
		return "P"
	elif(string == "Vice President"):
		return "V"
	elif(string == "Secretary"):
		return "S"
	elif(string == "Treasurer"):
		return "T"
	elif(string == "ALC"):
		return "A"
	elif(string == "Computer"):
		return "m"
	elif(string == "Constitution and Historian"):
		return "n"
	elif(string == "Recruitment"):
		return "r"
	elif(string == "House Improvements"):
		return "h"
	elif(string == "Project"):
		return "j"
	elif(string == "Public Relations"):
		return "b"
	elif(string == "Social"):
		return "s"
	elif(string == "Freshman Rep"):
		return "f"
	elif(string == "Off-Floor"):
		return "o"
	elif(string == "RA"):
		return "R"
	elif(string == "Off-Floor Rep"):
		return "O"
	else:
		return ''

