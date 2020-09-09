def insertion_sort(array):
	if len(array) == 0 or len(array) == 1:
		return array
	else:
		x = 0
		for i in range(x + 1, len(array)):
			current_item = array[i]
			j = i - 1
			while j >= 0 and array[j] > current_item:
				array[j + 1] = array[j]
				j -= 1
			array[j+1] = current_item
		return array
