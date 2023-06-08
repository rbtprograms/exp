def recurse_prod(a,b):
  # recursively multiply two positive integrers using only addition and subtraction (b >= 1)
  if b == 1:
    return a
  return a + recurse_prod(a, b - 1)

print(recurse_prod(12,3))