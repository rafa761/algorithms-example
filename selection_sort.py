unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]


def selection_sort(num_list):
	# We use len-1 because once we only have one item left in an unsorted list we assume it is sorted
	indexing_length = range(0, len(num_list) - 1)

	for i in indexing_length:
		min_value = i  # for each iteration store the first element as the minimum value

		# Inner loop to compare the rest of the list
		# range(i+1 to iterate trough the elements on the right
		for j in range(i + 1, len(num_list)):
			# If the element on current position is smaller than the stored minimum value
			if num_list[j] < num_list[min_value]:
				min_value = j  # store the new minimum value

		# To end the current inner loop iteration
		if min_value != i:
			num_list[min_value], num_list[i] = num_list[i], num_list[min_value]

	return num_list


if __name__ == '__main__':
	print('Before:', unsorted_list)
	print('After: ', selection_sort(unsorted_list))
