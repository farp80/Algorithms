class SearchingAlgorithms:

	def __init__(self, array, searching_query):
		self.searching_query = searching_query
		self.array = array
		self.__UNDEFINED = -1

	def get_searching_algorithms(self, algorithm):
		if algorithm == 'linear_search':
			return self._linear_search()
		elif algorithm == 'binary_search_recursive':
			right = len(self.array)
			left = 0
			#return self._binary_search_recursive(right, left)
			return self._binary_search(right, left)

	def _linear_search(self) -> object:
		for item in range(len(self.array)):
			if self.array[ item ] == self.searching_query:
				return item
		return self.__UNDEFINED

	def _binary_search_recursive(self, right: int, left: int) -> object:
		"""
			Binary Search Algorithm works perfect when the array is sorted,
			if it is not sorted then we need to sort it first and then perform the search.
		:param right:
		:param left:
		:return: it returns the index of the query param.
		"""
		if right < left:
			return self.__UNDEFINED

		middle_item = (right + left) // 2
		middle_value = self.array[middle_item]

		if self.searching_query == middle_value:
			return middle_item

		if self.array[middle_item ] > self.searching_query:
			self.array = self.array[ slice(middle_item) ]
			print(self.array)
			return self._binary_search_recursive(middle_item, left)

		return self._binary_search_recursive(middle_item + 1, right)

	def _binary_search(self, right, left):
		while left < right:
			middle = (left + right) // 2

			if self.array[middle] == self.searching_query:
				return middle

			if self.searching_query < self.array[middle]:
				right = middle - 1
			else:
				left = middle + 1
		return self.__UNDEFINED

