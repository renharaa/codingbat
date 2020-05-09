def double_char(str):
	"""
	Given a string, return a string where for every char in the original, there are two chars.

	double_char('The') → 'TThhee'
	double_char('AAbb') → 'AAAAbbbb'
	double_char('Hi-There') → 'HHii--TThheerree'
	"""
	
	new_str = ""
	for c in str:
		new_str += c*2
	return new_str

#######################################################################################

def count_hi(str):
	"""
	Return the number of times that the string "hi" appears anywhere in the given string.

	count_hi('abc hi ho') → 1
	count_hi('ABChi hi') → 2
	count_hi('hihi') → 2
	"""
	
	return str.count("hi")

#######################################################################################

def cat_dog(str):
	"""
	Return True if the string "cat" and "dog" appear the same number of times in the given string.

	cat_dog('catdog') → True
	cat_dog('catcat') → False
	cat_dog('1cat1cadodog') → True
	"""
	
	return str.count("cat") is str.count("dog")

#######################################################################################

def count_code(str):
	"""
	Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

	count_code('aaacodebbb') → 1
	count_code('codexxcode') → 2
	count_code('cozexxcope') → 2
	"""
	count = 0
	for i in range(len(str)-3):
		if str[i] is "c" and str[i+1] is "o" and str[i+3] is "e":
			count += 1
	return count
	
#######################################################################################

def end_other(a, b):
	"""
	Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

	end_other('Hiabc', 'abc') → True
	end_other('AbC', 'HiaBc') → True
	end_other('abc', 'abXabc') → True
	"""

	long_s, short_s = (a,b) if len(a) >= len(b) else (b,a)
	c = long_s.lower()
	d = short_s.lower()
  
	return c.endswith(d)

#######################################################################################
def xyz_there(str):
	"""
	Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

	xyz_there('abcxyz') → True
	xyz_there('abc.xyz') → False
	xyz_there('xyz.abc') → True
	"""

	for i in range(len(str)):
		if str[i] != '.' and str[i+1:i+4] == 'xyz':
			return True
  
	if str[0:3] == 'xyz':
		return True
	return False