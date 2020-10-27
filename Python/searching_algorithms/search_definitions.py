import time


class SearchingAlgorithms:

	def __init__(self, array = None, searching_query = None):
		self.searching_query = searching_query
		self.__array = array
		self.__UNDEFINED = -1
		self.__results = {}
		self.__recursive_iter = 0

	@property
	def results(self):
		return self.__results

	@results.setter
	def results(self, value):
		self.__results = value

	def get_searching_algorithms(self, algorithm):
		"""
			Get Searching Algorithms: It will get the algorithm name and process in different methods
			If the algorithm string is empty it won't execute any searching Algorithm.
		:param algorithm: search algorithm name.
		"""
		try:
			if algorithm is not None:
				if self.__array:
					right = len(self.__array)
					left = 0

				if algorithm == 'linear_search':
					self._linear_search()
				elif algorithm == 'binary_search_recursive':
					self._binary_search_recursive(right = right, left = left)
				elif algorithm == 'binary_search':
					self._binary_search(right = right, left = left)
				elif algorithm == 'negative_binary_search':
					self._negative_binary_search(right = right, left = left)
				elif algorithm == 'negative_linear_search':
					self._negative_linear_search()
				else:
					self._ternary_search(len(self.__array) - 1, 0)
		except Exception as e:
			print(f"Method: get_searching_algorithms failed: {e}")

	def _linear_search(self):
		"""
		   Linear Search: this method has an internal Array (unsorted).
		:return: True if the value was found.
		"""
		array = [ 1, 3, 6, 55, 89, 33, 157, 7, 5, 88, 33, 59, 11, 90, 333, 908, 90008, 1000 ]
		iteration = 0
		self.__results["value"] = self.__UNDEFINED
		self.__results[ "iterations" ] = iteration

		for item in range(len(array)):
			if array[item] == self.searching_query:
				self.__results["value"] = item
				self.__results["iterations"] = iteration
				return True
			iteration += 1
		return False

	def _binary_search_recursive(self, right: int, left: int) -> object:
		"""
			Binary Search Algorithm works perfect when the array is sorted,
			if it is not sorted then we need to sort it first and then perform the search.
		:param right:
		:param left:
		:return: it returns the index of the query param.
		"""
		self.__results["value"] = self.__UNDEFINED
		self.__recursive_iter += 1

		if right < left:
			return

		middle_item = (right + left) // 2
		middle_value = self.__array[ middle_item ]

		if self.searching_query == middle_value:
			self.__results["iterations"] = self.__recursive_iter
			self.__results["value"] = middle_item
			return

		if self.__array[middle_item] > self.searching_query:
			self.__array = self.array[slice(middle_item)]
			return self._binary_search_recursive(right = middle_item, left = left)

		return self._binary_search_recursive(right = right, left = middle_item + 1)

	def _binary_search(self, right, left):
		self.__results["value"] = self.__UNDEFINED

		while left < right:
			self.__recursive_iter += 1
			middle = (left + right) // 2

			if self.__array[middle] == self.searching_query:
				self.__results["value"] = middle
				self.__results["iterations"] = self.__recursive_iter
				return

			if self.searching_query < self.__array[middle]:
				right = middle - 1
			else:
				left = middle + 1
		return

	def _ternary_search(self, right, left):
		partition_size = (right - left) // 3
		mid_1 = left + partition_size
		mid_2 = right - partition_size
		self.__recursive_iter += 1

		self.__results["value"] = self.__UNDEFINED
		self.__results["iterations"] = self.__recursive_iter

		if left > right:
			return

		if self.__array[mid_1] == self.searching_query:
			self.__results["value"] = mid_1
			self.__results["iterations"] = self.__recursive_iter
			return

		if self.__array[mid_2] == self.searching_query:
			self.__results["value"] = mid_2
			self.__results["iterations"] = self.__recursive_iter
			return

		if self.searching_query < self.__array[mid_1]:
			return self._ternary_search(mid_1 - 1, left)

		if self.searching_query > self.__array[mid_2]:
			return self._ternary_search(right, mid_2 + 1)

		return self._ternary_search(mid_2 - 1, mid_1 + 1)

	def _negative_binary_search(self, right, left):
		"""
		 This function assumes that the array is sorted by all positive first and negative values
		 after. The goal is to look for the 1st negative value and then len(array) - index
		:param right:
		:param left:
		:return:
		"""
		self.__results["value"] = self.__UNDEFINED

		while left <= right:
			self.__recursive_iter += 1
			middle = (left + right) // 2

			if right == left:
				self.__results["value"] = right
				self.__results["iterations"] = self.__recursive_iter
				return

			if self.__array[middle] < 0:
				right = middle
			else:
				left = middle + 1

	def _negative_linear_search(self):
		for item in range(len(self.__array)):
			self.__recursive_iter += 1

			if self.__array[item] < 0:
				self.__results["iterations"] = self.__recursive_iter
				self.__results["value"] = item
				return
