"""
"""

import unittest

from genealogy import member


DEFAULT_NAME = "Default Name"


VALID_STRING_ATTRIB = 'Po'

INVALID_CHAR_ATTRIB = '0'
INVALID_EMPTY_ATTRIB = ''
INVALID_INT_ATTRIB = 0
INVALID_STRING_ATTRIB = '01'


class Constructor(unittest.TestCase):

	def test_constructor_passed_invalid_char(self):
		with self.assertRaises(ValueError):
			member.Member(DEFAULT_NAME, attributes=INVALID_CHAR_ATTRIB)

	def test_constructor_passed_invalid_string(self):
		with self.assertRaises(ValueError):
			member.Member(DEFAULT_NAME, attributes=INVALID_STRING_ATTRIB)

	def test_constructor_passed_wrong_type(self):
		with self.assertRaises(TypeError):
			member.Member(DEFAULT_NAME, attributes=INVALID_INT_ATTRIB)

	


class EmptyMember(unittest.TestCase):
	def setUp(self):
		self._member = member.Member(DEFAULT_NAME);

	# Default Vals
	def test_new_member_with_default_name_has_default_values(self):
		self.assertEqual(self._member.name, DEFAULT_NAME)
		self.assertFalse(self._member.nicknames)
		self.assertFalse(self._member.mentors)
		self.assertFalse(self._member.mentees)
		self.assertFalse(self._member.adoptors)
		self.assertFalse(self._member.adoptees)
		self.assertFalse(self._member.attributes)
	
	
	# Group Checkers
	def test_new_member_with_no_args_has_no_attributes(self):
		self.assertFalse(
				self._member.hasOneOf(member.Member.validAttributes),
				'Newly created member has valid attributes')

	def test_no_attribute_member_is_not_eboard(self):
		self.assertFalse(self._member.isEBoard())

	def test_no_attribute_member_is_not_cabinet(self):
		self.assertFalse(self._member.isCabinet())

	def test_no_attribute_member_is_not_off_floor(self):
		self.assertFalse(self._member.isOffFloor())

	def test_no_attribute_member_is_not_ra(self):
		self.assertFalse(self._member.isRA())

	# setAttribute
	def test_member_errors_on_invalid_char(self):
		with self.assertRaises(ValueError):
			self._member.setAttribute(INVALID_CHAR_ATTRIB)

	def test_member_errors_on_empty_attrib(self):
		with self.assertRaises(ValueError):
			self._member.setAttribute(INVALID_EMPTY_ATTRIB)

	def test_member_errors_on_invalid_string(self):
		with self.assertRaises(TypeError):
			self._member.setAttribute(INVALID_STRING_ATTRIB)

	def test_member_errors_on_invalid_attrib(self):
		with self.assertRaises(TypeError):
			self._member.setAttribute(VALID_STRING_ATTRIB)


	def test_member_errors_on_invalid_type(self):
		with self.assertRaises(TypeError):
			self._member.setAttribute(INVALID_INT_ATTRIB)



if __name__=='__main__':
	unittest.main()
