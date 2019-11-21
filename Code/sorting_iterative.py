#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) - iterate through each list item
    Memory usage: O(n)- only declaring one iterator (index)"""
    # Check that all adjacent items are in order, return early if so
    for index in range(len(items) -  1):
      if items[index] > items[index + 1]:
        return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: Best case O(n) - when input is sorted and no swaps are made
                  Worst case O(n^2) - must iterate through array n times
    Memory usage: O(1) - swaps happen in place"""
    # Repeat until all items are in sorted order
    # for index, item in enumerate(items):
    if len(items) <= 1:
      return items
    while not is_sorted(items):
      for index in range(len(items) - 1):
        if items[index] > items[index + 1]:
          # Swap adjacent items that are out of order
          items[index], items[index + 1] = items[index + 1], items[index]
    return items

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.

    Running time: O(n^2) in all cases because we need to find a new minimum 
    n times.

    Memory usage: O(1) because all of the swapping happens in place"""
    
    min_index = 0
    sorted_index = 0

    while sorted_index < len(items):
      min_index = sorted_index
    # Find minimum item in unsorted items
      for index in range(sorted_index, len(items)):
        if items[index] < items[min_index]:
          min_index = index

      # Swap it with first unsorted item
      items[sorted_index], items[min_index] = items[min_index], items[sorted_index]
      sorted_index += 1
    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.

    Running time: Best case O(n) - input is already sorted
                  Worst case O(n^2) - input requires maximum amount of swaps (reverse sorted)

    Memory usage: O(1) - sorting happens in place"""
    # keep track of the previous item"""
    # Repeat until all items are in sorted order
    for index in range(1, len(items)):
      #  Take first unsorted item
      item = items[index]
      rev_index = index - 1
      while rev_index >= 0 and item < items[rev_index]:
        items[rev_index + 1] = items[rev_index]
        rev_index -= 1
      items[rev_index + 1] = item
    return items

# if __name__ == '__main__':
#   nums = [4, 10, 2, 5 ,6, 3]
#   print(bubble_sort_slow(nums))

################################################################################
################################################################################
################################################################################

# TODO: COCKTAIL SORT!?!?!!?
# def bubble_sort_fast(items):
#     """This is an extra version of bubble sort using swaps instead of is_sorted, 
#     needs to be cocktail sort to pass all tests"""
#     # use number of swaps instead of is_sorted
#     swaps = 0
#     while swaps < 2:
#       # reset swaps before they occur
#       swaps = 0
#       sorted_spots = 1
#       for index in range(len(items) - sorted_spots):
#         if items[index] > items[index + 1]:
#           # Swap adjacent items that are out of order
#           items[index], items[index + 1] = items[index + 1], items[index]
#           swaps += 1
#           sorted_spots += 1
#     return items
