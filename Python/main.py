from searching_algorithms.search_definitions import SearchingAlgorithms
from sort_algorithms.sorting_definitions import SortingAlgorithmsDefinition


searching_algorithms_compute = [ ]
sorting_algorithms_compute = [ ]


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


def process_sorting_algorithms():
	settings = [
		{"algorithm": "bubble_sort", "array": [16, 6000, 11000, 856, 70007, 12, 15, 1008, 5, 33, 5, 90, 908, 20000, 60000]},
		# {"algorithm": "bucket_sort", "array": [16, 6000, 11000, 856, 70007, 12, 15, 1008, 5, 33, 5, 90, 908, 20000, 60000]},
		{"algorithm": "counting_sort", "array": [5, 1, 2, 5, 5, 4, 1, 0, 0, 1, 1, 3], "sort_range": 5},
		{"algorithm": "insertion_sort", "array": [16, 6000, 11000, 856, 70007, 12, 15, 1008, 5, 33, 5, 90, 908, 20000, 60000]},
		{"algorithm": "merge_sort", "array": [16, 6000, 11000, 856, 70007, 12, 15, 1008, 5, 33, 5, 90, 908, 20000, 60000]},
		{"algorithm": "quick_sort", "array": [16, 6000, 11000, 856, 70007, 12, 15, 1008, 5, 33, 5, 90, 908, 20000, 60000]},
		{"algorithm": "selection_sort", "array": [16, 6000, 11000, 856, 70007, 12, 15, 1008, 5, 33, 5, 90, 908, 20000, 60000]},
		]

	for algorithm in settings:
		if algorithm["algorithm"] == 'counting_sort':
			sorting_definition = SortingAlgorithmsDefinition(
				algorithm[ "algorithm" ],
				array = algorithm[ "array" ],
				sort_range = algorithm["sort_range"])
		else:
			sorting_definition = SortingAlgorithmsDefinition(algorithm["algorithm"], array=algorithm["array"])
		result = sorting_definition.get_sorting_algorithm()
		sorting_algorithms_compute.append({
			"algorithm": algorithm["algorithm"],
			"iterations": result["iterations"]
			})


if __name__ == '__main__':
	# process_searching_algorithms()
	process_sorting_algorithms()
