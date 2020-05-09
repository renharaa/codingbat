def first_last6(nums):
	"""
	Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

	first_last6([1, 2, 6]) → True
	first_last6([6, 1, 2, 3]) → True
	first_last6([13, 6, 1, 2, 3]) → False
	"""
	
	return 6 in [nums[0],nums[-1]]

#################################################################

def same_first_last(nums):
	"""
	
	Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

	same_first_last([1, 2, 3]) → False
	same_first_last([1, 2, 3, 1]) → True
	same_first_last([1, 2, 1]) → True
	"""
	
	return len(nums) > 0 and nums[-1] is nums[0]

#################################################################

def make_pi():
	"""
	Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

	make_pi() → [3, 1, 4]
	"""
	
	return [3,1,4]

#################################################################

def common_end(a, b):
	"""
	Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

	common_end([1, 2, 3], [7, 3]) → True
	common_end([1, 2, 3], [7, 3, 2]) → False
	common_end([1, 2, 3], [1, 3]) → True
	"""
	
	return a[0] is b[0] or a[-1] is b[-1]

#################################################################

def sum3(nums):
	"""
	Given an array of ints length 3, return the sum of all the elements.

	sum3([1, 2, 3]) → 6
	sum3([5, 11, 2]) → 18
	sum3([7, 0, 0]) → 7
	"""
	
	return sum(nums)
	
#################################################################

def rotate_left3(nums):
	"""
	Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

	rotate_left3([1, 2, 3]) → [2, 3, 1]
	rotate_left3([5, 11, 9]) → [11, 9, 5]
	rotate_left3([7, 0, 0]) → [0, 0, 7]
	"""
	
	return [nums[1],nums[2],nums[0]]

#################################################################

def reverse3(nums):
	"""
	Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

	reverse3([1, 2, 3]) → [3, 2, 1]
	reverse3([5, 11, 9]) → [9, 11, 5]
	reverse3([7, 0, 0]) → [0, 0, 7]
	"""
	
	return [nums[2], nums[1], nums[0]]

#################################################################

def max_end3(nums):
	"""
	Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

	max_end3([1, 2, 3]) → [3, 3, 3]
	max_end3([11, 5, 9]) → [11, 11, 11]
	max_end3([2, 11, 3]) → [3, 3, 3]
	"""
	
	return [nums[0]] * 3 if nums[0] > nums[2] else [nums[2]] * 3

#################################################################

def sum2(nums):
	"""
	Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

	sum2([1, 2, 3]) → 3
	sum2([1, 1]) → 2
	sum2([1, 1, 1, 1]) → 2
	"""
	
	return sum(nums[:2])

#################################################################

def middle_way(a, b):
	"""
	Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

	middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
	middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
	middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
	"""
	
	return [ a[1] , b[1] ]

#################################################################

def make_ends(nums):
	"""
	Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

	make_ends([1, 2, 3]) → [1, 3]
	make_ends([1, 2, 3, 4]) → [1, 4]
	make_ends([7, 4, 6, 2]) → [7, 2]
	"""
	
	return [ nums[0] , nums[-1] ]

#################################################################
def has23(nums):
	"""
	Given an int array length 2, return True if it contains a 2 or a 3.

	has23([2, 5]) → True
	has23([4, 3]) → True
	has23([4, 5]) → False
	"""
	
	return 2 in nums or 3 in nums