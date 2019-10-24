#!python

def min_max(numbers):
    """Helper function to find range of list"""
    min_val = min(numbers)
    max_val = max(numbers)
    return (min_val, max_val)

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    rng = min_max(numbers)

    # Create list of counts with a slot for each number in input range
    counts = [0] * (rng[1] - rng[0] + 1)

    # Loop over given numbers and increment each number's count
    for num in numbers:
      index = num - rng[0]
      counts[index] += 1

    new_items = []
    #  Loop over counts and append that many numbers into output list
    for index in range(len(counts)):
      num = rng[0] + index
      nums = [num] * counts[index]
      new_items.extend(nums)
    # FIXME: Improve this to mutate input instead of creating new output list
    return new_items


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

if __name__ == '__main__':
  numbers = [2, 1, 4, 7, 6, 2, 1, 2]
  print(counting_sort(numbers))