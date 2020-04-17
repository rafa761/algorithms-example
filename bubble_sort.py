unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]


def bubble_sort(num_list):
	# We can't compare the number after que last index, so we use len-1 because there's no number there
	indexing_length = len(num_list) - 1
	sorted = False  # variable to be used inside of the control flow to know when the list is sorted

	# we need to perform an unknown number of iterations
	while not sorted:
		sorted = True

		for i in range(0, indexing_length):
			# If the number on the left is greater than the number on the right
			if num_list[i] > num_list[i + 1]:
				sorted = False

				# Switch elements
				num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

	return num_list


if __name__ == '__main__':
	print('Before:', unsorted_list)
	print('After: ', bubble_sort(unsorted_list))
