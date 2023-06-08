def recurse_sum_list(a, n):
  # recursively sum a list up to n elements when n>=1
  if n == 1:
    return a[0]
  return a[0] + recurse_sum_list(a[1:], n-1)

print(recurse_sum_list([1,2,3,4,5,6],3))