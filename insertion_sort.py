unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]


def insertion_sort(num_list):
	# We don't need to consider the index 0 because there isn't any number on the left
	for i in range(1, len(num_list)):
		# store the current value to sort
		value_to_sort = num_list[i]

		# While there are greater values on the left
		while num_list[i - 1] > value_to_sort and i > 0:
			# switch the values
			num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
			i -= 1

	return num_list


if __name__ == '__main__':
	print('Before:', unsorted_list)
	print('After: ', insertion_sort(unsorted_list))
