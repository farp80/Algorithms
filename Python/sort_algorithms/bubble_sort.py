def bubble_sort(unsorted_array):
	if len(unsorted_array) == 0:
		return unsorted_array
	elif len(unsorted_array) == 1:
		return unsorted_array
	else:
		for i in range(len(unsorted_array)):
			is_sorted = True
			for j in range(len(unsorted_array) - 1 - i):
				if unsorted_array[j] > unsorted_array[j+1]:
					swap(unsorted_array, j, j + 1)
					is_sorted = False
			if is_sorted:
				return unsorted_array
	return unsorted_array


def swap(unsorted_array, index1, index2):
	temp = unsorted_array[index2]
	unsorted_array[index2] = unsorted_array[index1]
	unsorted_array[index1] = temp
