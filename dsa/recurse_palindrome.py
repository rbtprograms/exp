def recurse_palindrome(a):
  if len(a) <= 1:
    return True
  if a[0] != a[-1]:
    return False
  return recurse_palindrome(a[1:len(a)-1])

print(recurse_palindrome('gohangasalamiimalaagnahog'))