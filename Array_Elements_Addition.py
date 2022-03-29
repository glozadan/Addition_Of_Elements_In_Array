#Function that adds up every element in an array of lenght less than 1000 elements
def Array_Addition(array):
  total = 0
  if len(array) < 1000:
    for i in array:
      total += i
    return total
