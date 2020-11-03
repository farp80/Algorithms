class SortingAlgorithmsDefinition:

	def __init__(self, algorithm: str, array = None, sort_range: int = None):
		"""

		:param algorithm:
		:param array:
		:param sort_range:
		"""
		self.__algorithm = algorithm
		self.__results = {}
		self.__iterations = 0

		if array:
			self.__array = array

		if sort_range:
			self.__sort_range = sort_range

	def get_sorting_algorithm(self):
		if self.__algorithm == 'bubble_sort':
			return self._bubble_sort()
		elif self.__algorithm == 'bucket_sort':
			pass
		elif self.__algorithm == 'counting_sort':
			return self._counting_sort()
		elif self.__algorithm == 'insertion_sort':
			return self._insertion_sort()
		elif self.__algorithm == 'merge_sort':
			return self._merge_sort()
		elif self.__algorithm == 'quick_sort':
			start = 0
			end = len(self.__array) - 1
			return self._quick_sort(start, end)
		else:
			return self._selection_sort()

	def _bubble_sort(self):
		if len(self.__array) == 0 or len(self.__array) == 1:
			self.__results["result"] = self.__array
			self.__results["iterations"] = self.__iterations
		else:
			for i in range(len(self.__array)):
				self.__iterations += 1
				is_sorted = True
				for j in range(len(self.__array) - 1 - i):
					self.__iterations += 1
					if self.__array[ j ] > self.__array[ j + 1 ]:
						self._swap(j, j + 1)
						is_sorted = False
				if is_sorted:
					self.__results["iterations"] = self.__iterations
					self.__results["result"] = self.__array
		return self.__results

	def _bucket_sort(self):
		pass

	def _quick_sort(self, start, end):
		if start >= end:
			self.__results["iterations"] = self.__iterations
			self.__results["result"] = self.__array
			return self.__results
		# select a pivot (usually the last element)
		# Partition
		boundary = self._partition(start, end)
		# sort left
		self._quick_sort(start, boundary - 1)
		# sort right
		self._quick_sort(boundary + 1, end)

		self.__results["iterations"] = self.__iterations
		self.__results["result"] = self.__array
		return self.__results

	def _selection_sort(self):
		if len(self.__array) == 0 or len(self.__array) == 1:
			self.__results["iterations"] = self.__iterations
			self.__results["result"] = self.__array
			return self.__results
		else:
			for i in range(len(self.__array)):
				self.__iterations += 1
				min_index = i
				for j in range(i + 1, len(self.__array)):
					self.__iterations += 1
					if self.__array[j] < self.__array[min_index]:
						min_index = j
				self._swap(min_index, i)

			self.__results["iterations"] = self.__iterations
			self.__results["result"] = self.__array
			return self.__results

	def _insertion_sort(self):
		if len(self.__array) == 0 or len(self.__array) == 1:
			self.__results["result"] = self.__array
			self.__results["iterations"] = self.__iterations
		else:
			x = 0
			for i in range(x + 1, len(self.__array)):
				self.__iterations += 1
				current_item = self.__array[i]
				j = i - 1
				while j >= 0 and self.__array[j] > current_item:
					self.__iterations += 1
					self.__array[j + 1] = self.__array[j]
					j -= 1
				self.__array[j + 1] = current_item

			self.__results[ "iterations" ] = self.__iterations
			self.__results["result"] = self.__array
			return self.__results

	def _counting_sort(self):
		# It is suitable most of the time when all the values in a range
		# are present in the array, for example:
		# range (0-5) --> [4,5,1,2,3,5,2,1,0]
		# range is referring to the values of the index not to the length of the array.
		count_array = [ 0 for i in range(self.__sort_range + 1) ]
		for i in range(len(self.__array)):
			count_array[ self.__array[ i ] ] += 1

		k = 0
		for i in range(len(count_array)):
			self.__iterations += 1
			for j in range(count_array[ i ]):
				self.__iterations += 1
				self.__array[ k ] = i
				k += 1

		self.__results["iterations"] = self.__iterations
		self.__results["result"] = self.__array
		return self.__results

	def _merge_sort(self):
		if len(self.__array) == 0 or len(self.__array) == 1:
			return array

		half = len(self.__array) // 2
		left = []

		for i in range(half):
			left.append(self.__array[i])

		right = []

		for j in range(half, len(self.__array)):
			right.append(self.__array[j])

		left.sort()
		right.sort()

		self._merge(left, right)
		self.__results[ "iterations" ] = self.__iterations
		self.__results["results"] = self.__array
		return self.__results

	def _partition(self, start, end):
		"""

		:param array:
		:param start:
		:param end: index of the last item in the array.
		:return:
		"""
		# last item in the array.
		pivot = self.__array[ end ]
		boundary = start - 1

		for i in range(start, end + 1):
			self.__iterations += 1
			if self.__array[ i ] <= pivot:
				boundary += 1
				self._swap(i, boundary)

		return boundary

	def _swap(self,  index1, index2):
		temp = self.__array[index2]
		self.__array[index2] = self.__array[ index1]
		self.__array[index1] = temp

	def _merge(self, left, right):
		i = 0
		j = 0
		k = 0

		while i < len(left) and j < len(right):
			self.__iterations += 1
			if left[i] <= right[j]:
				self.__array[k] = left[i]
				k += 1
				i += 1
			else:
				self.__array[k] = right[j]
				k += 1
				j += 1

		while i < len(left):
			self.__iterations += 1
			self.__array[k] = left[i]
			k += 1
			i += 1

		while j < len(right):
			self.__iterations += 1
			self.__array[k] = right[j]
			k += 1
			j += 1
