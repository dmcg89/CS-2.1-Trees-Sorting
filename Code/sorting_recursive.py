#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    i = 0
    j = 0
    merged_list = []
    #  Repeat until one list is empty
    while i < len(items1) and j < len(items2):
    #  Find minimum item in both lists and append it to new list
      if items1[i] == items2[j]:
        merged_list.append(items1[i])
        merged_list.append(items1[i])
        i += 1
        j += 1
      elif items1[i] < items2[j]:
        merged_list.append(items1[i])
        i += 1
      elif items1[i] > items2[j]:
        merged_list.append(items2[j])
        j+= 1
    #  Append remaining items in non-empty list to new list
    if i < len(items1):
      for index in range(i, len(items1)):
        merged_list.append(items1[index])
    else:
      for index in range(j, len(items2)):
        merged_list.append(items2[index])
    return merged_list

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Memory usage: ??? Why and under what conditions?"""
    #  Split items list into approximately equal halves
    mid_i = len(items) // 2
    items1, items2 = items[:mid_i], items[mid_i:]
    #  Sort each half using any other sorting algorithm
    items1, items2 = sorted(items1), sorted(items2)
    #  Merge sorted halves into one list in sorted order
    return_list = merge(items1, items2)
    return return_list


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #  Check if list is so small it's already sorted (base case)
    if len(items) <= 1: return items 
    #  Split items list into approximately equal halves
    items1, items2 = items[:len(items) // 2], items[len(items) // 2:]
    #  Sort each half by recursively calling merge sort
    left, right = merge_sort(items1), merge_sort(items2)
    #  Merge sorted halves into one list in sorted order
    items[:] = merge(left, right)
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #  Choose a pivot any way and document your method in docstring above
    pivot = low
    moved_items = 0
    #  Loop through all items in range [low...high]
    for index in range(low, high):
      # print(items)
    #  Move items less than pivot into front of range [low...p-1]
      if items[index] < items[pivot]:
        moved_items += 1
        items[pivot + moved_items], items[index] = items[index], items[pivot + moved_items]
    #  TODO:  Move items greater than pivot into back of range [p+1...high] (pivot chosen as low, does not apply)
      # if items[index] > items[pivot]:

    #  Move pivot item into final position [p] and return index p
    items[pivot], items[pivot + moved_items] =items[pivot + moved_items], items[pivot]
    # print(f'items: {items}')
    return pivot + moved_items




def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #  Check if list or range is so small it's already sorted (base case)
    #  Check if high and low range bounds have default values (not given)
    #  Select arbitrary pivot point (first item)
    if len(items) <= 1:
      return
    if low == None and high == None:
      high = len(items)
      low = 0
      quick_sort(items, low, high)
      # return
    elif high - low == 0: return items
    #  Partition items in-place around a pivot and get index of pivot
    pivot = partition(items, low, high)
    # print(low,pivot,high)
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, pivot)
    quick_sort(items, pivot + 1, high)


# items1 = [3, 5, 7, 8]
# items2 = [9, 21, 4, 7, 9, -3, 5, -1, 6, 8, 20]

# # print(items2)
# # print(partition(items2, 0, len(items2)))
# # print(items2)
# quick_sort(items2)
# print(items2)



