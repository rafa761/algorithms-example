unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]


def linear_search(num_list, number_to_find):
	# We iterate trough the list
	for number in num_list:
		# Check if each number is equal to que number we are searching for
		if number == number_to_find:
			return f'{number} is in the list'

	# If get out of the loop means that the number is not found
	return f'{number_to_find} is not on the list'


if __name__ == '__main__':
	print('List:', unsorted_list)
	print('Element found: ', linear_search(unsorted_list, 8))
	print('Element not found: ', linear_search(unsorted_list, 92))
