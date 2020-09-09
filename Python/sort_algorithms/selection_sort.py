def selection_sort(array):
	if len(array) == 0 or len(array) == 1:
		return array
	else:
		for i in range(len(array)):
			min_index = i
			for j in range(i + 1, len(array)):
				if array[j] < array[min_index]:
					min_index = j
			swap(array, min_index, i)
		return array


def swap(unsorted_array, index1, index2):
	temp = unsorted_array[index2]
	unsorted_array[index2] = unsorted_array[index1]
	unsorted_array[index1] = temp
