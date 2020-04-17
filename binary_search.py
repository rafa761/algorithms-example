sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(num_list, number_to_find):
	# to find the middle we need to know the begining and the end of the list
	begin_index = 0
	end_index = len(num_list) - 1

	while begin_index <= end_index:
		# Find the mid point in the list
		midpoint = begin_index + (end_index - begin_index) // 2

		# get the midpoint value in the list
		midpoint_value = num_list[midpoint]

		# Chek if the number in the midpoint is equal to the number we are searching
		if midpoint_value == number_to_find:
			return midpoint

		# If the number searched is smaller than the midpoint
		# then we need to search the left part of the list
		elif number_to_find < midpoint_value:
			end_index = midpoint - 1

		# If the number searched is greated we need to search the right part of the list
		else:
			begin_index = midpoint + 1

	# If not found return None
	return None


if __name__ == '__main__':
	print('List:', sorted_list)
	print(f'Element {8} found at index {binary_search(sorted_list, 8)} on the list')
	print(f'Element {92} not found: {binary_search(sorted_list, 92)}')
