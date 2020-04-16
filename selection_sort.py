unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]


def selection_sort(num_list):
	# Outer loop
	for i in range(0, len(num_list) - 1):
		min_index = i  # Store the actual minimum index

		# The inner loop iterate over unsorted part of the list
		for j in range(i + 1, len(num_list)):
			# Compare to find the minimum item
			if num_list[j] < num_list[min_index]:
				min_index = j  # Save the index of minimum item
		# Swap the item in the place
		if min_index != i:
			num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

	return num_list


if __name__ == '__main__':
	print('Before:', unsorted_list)
	print('After: ', selection_sort(unsorted_list))
