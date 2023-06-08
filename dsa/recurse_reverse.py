def recurse_reverse(a):
  if len(a) == 0:
    return ''
  recurse_reverse(a[1:])
  print(a[0], end = '')

recurse_reverse('pots&pans')