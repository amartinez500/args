#args mean I can use as many arguments as possible

def sum(*args):
  total = 0
  for arg in args :
    total += arg
  return total
    
  
print(sum(3,3,4,5,6,7,8,9))

#kwargs means using key values(limitless)
#its a step beyond args
#keys and values represented **
def a_sum(**kwargs):
  total = 0
  for key,value in kwargs.items():
    print(f'{key} = {value}')
    total += value
  return total

print(a_sum(x=3,y=5,z=22))