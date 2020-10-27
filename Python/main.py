from sort_algorithms.bubble_sort import bubble_sort
from sort_algorithms.selection_sort import selection_sort
from sort_algorithms.insertion_sort import insertion_sort
from sort_algorithms.merge_sort import merge_sort
from sort_algorithms.quick_sort import quick_sort
from sort_algorithms.couting_sort import counting_sort
from searching_algorithms.search_definitions import SearchingAlgorithms


searching_algorithms_compute = [ ]


def process_searching_algorithms():
	array_sorted = [ 1, 3, 6, 7, 12, 15, 26, 55, 33, 59, 90, 333, 908, 1008, 11000, 20000, 60000 ]
	array_with_negative = [ 9, 4, 6, 33, 0, 12, -9, -1, -7, -3 ]

	settings_searching = [
		{"algorithm": 'linear_search', "array": None, "searching_query": 1000},
		{"algorithm": 'binary_search_recursive', "array": array_sorted, "searching_query": 60000},
		{"algorithm": 'binary_search', "array": array_sorted, "searching_query": 60000},
		{"algorithm": 'ternary_search', "array": array_sorted, "searching_query": 60000},
		{"algorithm": 'negative_binary_search', "array": array_with_negative, "searching_query": None},
		{"algorithm": 'negative_linear_search', "array": array_with_negative, "searching_query": None}
		]

	for item in settings_searching:
		current_algorithm = SearchingAlgorithms(array = item[ "array" ], searching_query = item[ "searching_query" ])
		current_algorithm.get_searching_algorithms(item[ "algorithm" ])

		searching_algorithms_compute.append({
			"algorithm": item[ "algorithm" ],
			"index": current_algorithm.results[ "value" ],
			"iterations": current_algorithm.results[ "iterations" ]
			})


# def sort_array(name):
# 	unsorted_array = [ 120, 2, 0, 234, 1 ]
# 	if name == 'bubble_sort':
# 		return bubble_sort(unsorted_array)
# 	elif name == 'selection_sort':
# 		return selection_sort(unsorted_array)
# 	elif name == 'insertion_sort':
# 		return insertion_sort(unsorted_array)
# 	elif name == 'merge_sort':
# 		return merge_sort(unsorted_array)
# 	elif name == 'quick_sort':
# 		return quick_sort(unsorted_array, 0, 4)
# 	elif name == 'counting_sort':
# 		return counting_sort([ 5, 1, 2, 5, 5, 4, 1, 0, 0, 1, 1, 3 ], 5)

if __name__ == '__main__':
	process_searching_algorithms()
