def merge_sort(array):
	if len(array) == 0 or len(array) == 1:
		return array

	half = len(array) // 2
	left = []

	for i in range(half):
		left.append(array[i])

	right = []

	for j in range(half, len(array)):
		right.append(array[j])

	left.sort()
	right.sort()

	merge(left, right, array)

	return array


def merge(left, right, result):
	i = 0
	j = 0
	k = 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result[k] = left[i]
			k += 1
			i += 1
		else:
			result[k] = right[j]
			k += 1
			j += 1

	while i < len(left):
		result[k] = left[i]
		k += 1
		i += 1

	while j < len(right):
		result[k] = right[j]
		k += 1
		j += 1




