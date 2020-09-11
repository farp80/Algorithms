def quick_sort(array, start, end):
	if start >= end:
		return
	# select a pivot (usually the last element)
	# Partition
	boundary = partition(array, start, end)
	# sort left
	quick_sort(array, start, boundary - 1)
	# sort right
	quick_sort(array, boundary + 1, end)
	return array


def partition(array, start, end):
	"""

	:param array:
	:param start:
	:param end: index of the last item in the array.
	:return:
	"""
	# last item in the array.
	pivot = array[end]
	boundary = start - 1

	for i in range(start, end + 1):
		if array[i] <= pivot:
			boundary += 1
			swap(array, i, boundary)

	return boundary


def swap(unsorted_array, index1, index2):
	temp = unsorted_array[index2]
	unsorted_array[index2] = unsorted_array[index1]
	unsorted_array[index1] = temp


