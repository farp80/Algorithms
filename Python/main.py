from sort_algorithms.bubble_sort import bubble_sort
from sort_algorithms.selection_sort import selection_sort
from sort_algorithms.insertion_sort import  insertion_sort
from sort_algorithms.merge_sort import  merge_sort
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sort_array(name):
    unsorted_array = [120,2, 0, 234,1]
    if name == 'bubble_sort':
        return bubble_sort(unsorted_array)
    elif name == 'selection_sort':
        return selection_sort(unsorted_array)
    elif name == 'insertion_sort':
        return insertion_sort(unsorted_array)
    elif name == 'merge_sort':
        return merge_sort(unsorted_array)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sorted_array = sort_array('merge_sort')
    print(sorted_array)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
