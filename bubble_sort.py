unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]


def bubble_sort(num_list):
	# Outer loop
	for i in range(0, len(num_list) - 1):
		# The inner loop iterate over the list to compare
		for j in range(0, len(num_list) - 1 - i):
			# Compare the numbers
			if num_list[j] > num_list[j + 1]:
				# swap if it is necessary
				num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

	return num_list


if __name__ == '__main__':
	print('Before:', unsorted_list)
	print('After: ', bubble_sort(unsorted_list))
