unsorted_list = [7, 3, 9, 2, 8, 4, 1, 5, 6]


def insertion_sort(num_list):
	# Outer loop starts on the second element of the list
	for i in range(1, len(num_list)):
		# The inner loop start on i-1 and iterate backwards
		for j in range(i - 1, -1, -1):
			# If the item on the right is less than the item on the left
			if num_list[j] > num_list[j + 1]:
				num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
			# If not break the inner loop
			else:
				break

	return num_list


if __name__ == '__main__':
	print('Before:', unsorted_list)
	print('After: ', insertion_sort(unsorted_list))
