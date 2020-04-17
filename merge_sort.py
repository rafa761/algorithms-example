unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]


def merge_sort(num_list):
	# Condition to divide the list and stop recursion
	if len(num_list) > 1:
		mid = len(num_list) // 2
		left_list = num_list[:mid]  # left list contains start to the middle element
		right_list = num_list[mid:]  # right list contains middle to end elements

		# Use recursion to create more sublists
		merge_sort(left_list)
		merge_sort(right_list)

		# Initialize the indexes used to sort and merge
		index_left = index_right = index_merge = 0

		# Condition to Merge. We need to execute the sort until reach the end of the sublists
		while index_left < len(left_list) and index_right < len(right_list):
			# Compares if the left list element is smaller
			if left_list[index_left] < right_list[index_right]:
				num_list[index_merge] = left_list[index_left]  # insert the element in the main list
				index_left += 1

			# If the left list element not is the smaller
			else:
				num_list[index_merge] = right_list[index_right]
				index_right += 1

			# increment the index of the main list
			index_merge += 1

		# Condition to check remaining elements in case of sublists with different lengths
		while index_left < len(left_list):
			num_list[index_merge] = left_list[index_left]
			index_left += 1
			index_merge += 1

		# We need to check on both left and right list for remaining elements
		while index_right < len(right_list):
			num_list[index_merge] = right_list[index_right]
			index_right += 1
			index_merge += 1

	return num_list


if __name__ == '__main__':
	print('Before:', unsorted_list)
	print('After: ', merge_sort(unsorted_list))
