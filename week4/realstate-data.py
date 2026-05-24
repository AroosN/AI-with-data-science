import numpy as np


status , price , city, prev_sold_date = np.genfromtxt('week4/RealEstate-USA.csv', delimiter = ',', usecols = (1 , 2, 6, 11) , unpack = True, dtype =None , skip_header = 1)

print(status)
print(price)
print(city)
print(prev_sold_date)

