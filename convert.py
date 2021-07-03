import math

def convert(base, number)
  a = str(number)
  length = len(a)
  deci = 0
  for x in range(1,length+1):
      coef=float(a[length-x])
      exp=float(x-1)
      deci = deci+coef*math.pow(base,exp)
  return deci
