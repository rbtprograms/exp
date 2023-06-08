from math import inf

def recurse_extrema(a, largest = -inf, smallest=inf):
  current_largest, current_smallest = largest, smallest
  # recursively find the largest element of a list
  if len(a) == 0:
    return (largest, smallest)
  if a[0] > largest:
    current_largest = a[0]
  if a[0] < smallest:
    current_smallest = a[0]
  return recurse_extrema(a[1:], largest=current_largest, smallest=current_smallest)

print(recurse_extrema([1,2,6,4,5,3]))