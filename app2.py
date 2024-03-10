from data.geo2 import Location
import pandas as pd


data = []
for _ in range(1,350000):
    local = Location.random_location()
    data.append(local)
  #  print(local)
    
df = pd.DataFrame(data)

df.to_csv('DATA_SET/Random_Cities.csv', index=False)
    
