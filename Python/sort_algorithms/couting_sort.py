def counting_sort(array, max_value):
	# It is suitable most of the time when all the values in a range
	# are present in the array, for example:
	# range (0-5) --> [4,5,1,2,3,5,2,1,0]
	# range is referring to the values of the index not to the length of the array.
	count_array = [0 for i in range(max_value + 1)]
	for i in range(len(array)):
		count_array[array[i]] += 1

	k = 0
	for i in range(len(count_array)):
		for j in range(count_array[i]):
			array[k] = i
			k += 1

	return array
