#args mean I can use as many arguments as possible

def sum(*args):
  total = 0
  for arg in args :
    total += arg
  return total
    
  
print(sum(3,3,4,5,6,7,8,9))

#kwargs means using key values(limitless)