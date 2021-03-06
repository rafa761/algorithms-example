unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def merge_sort(num_list):
	# Condition to stop recursion
	if len(num_list) <= 1:
		return num_list

	mid = len(num_list) // 2

	# Use recursion to create sub lists
	left_list, right_list = merge_sort(num_list[:mid]), merge_sort(num_list[mid:])

	return merge(left_list, right_list)


def merge(left_list, right_list):
	result_list = []

	# Initialize the indexes used to sort and merge
	index_left = index_right = 0

	# We need to execute the sort until reach the end of the sub-lists
	while index_left < len(left_list) and index_right < len(right_list):
		# Compares if the left list element is smaller
		if left_list[index_left] < right_list[index_right]:
			result_list.append(left_list[index_left])
			index_left += 1

		# If the left list element not is the smaller
		else:
			result_list.append(right_list[index_right])
			index_right += 1

	# add the remaining elements to the result list
	result_list.extend(left_list[index_left:])
	result_list.extend(right_list[index_right:])

	return result_list


if __name__ == '__main__':
	print('-=' * 5, 'Sorted List', '-=' * 5)
	print('Before:', sorted_list)
	print('After: ', merge_sort(sorted_list))
	print('\n')

	print('-=' * 5, 'Reverse List', '-=' * 5)
	print('Before:', reverse_list)
	print('After: ', merge_sort(reverse_list))
	print('\n')

	print('-=' * 5, 'Unsorted List', '-=' * 5)
	print('Before:', unsorted_list)
	print('After: ', merge_sort(unsorted_list))
