import numpy as np


status , price , city, prev_sold_date = np.genfromtxt('week4/RealEstate-USA.csv', delimiter = ',', usecols = (1 , 2, 6, 11) , unpack = True, dtype =None , skip_header = 1)

print(status)
print(price)
print(city)
print(prev_sold_date)

print ('RealEstate-USA.csv mean:' , np.mean(price))
print ('RealEstate-USA.csv median:' , np.median(price))
print ('RealEstate-USA.csv standard deviation:' , np.std(price))
print ('RealEstate-USA.csv variance' , np.var(price))
print ("RealEstate-USA.csv percentile - 25:", np.percentile(price, 25))
print ('RealEstate-USA.csv percentile - 3') , np.percentile(price,3)
print ('RealEstate-USA.csv min:', np.min(price))
print ('RealEstate-USA.csv max:' , np.max(price))


#math operations

