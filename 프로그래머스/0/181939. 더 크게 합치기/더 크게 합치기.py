def solution(a, b):
  a = str(a)
  b = str(b)
  ab = int(a + b)
  ba = int(b + a)
  if ab == ba:
    return ab
  else:
    return max(ab, ba)