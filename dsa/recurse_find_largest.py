def recurse_find_largest(a, largest = 0):
  current_largest = largest
  # recursively find the largest element of a list
  if len(a) == 0:
    return largest
  if a[0] > largest:
    current_largest = a[0]
  return recurse_find_largest(a[1:], largest=current_largest)

print(recurse_find_largest([1,2,6,4,5,3]))