import pandas as pd
import matplotlib.pyplot as plt
data = {
           "name":["ayushi","Ankita 1","Ankita 2","Susmita","arisha"],
           "age":[18,18,18,17,16],
           "math":[15,45,75,85,25],
           "C":[35,45,55,65,75] 
       }

df = pd.DataFrame(data)
print(df)

#6.a) Histogram
df['math'].plot(kind='hist', bins=5, color='red',edgecolor='black')
plt.title('Histogram - Close Values')
plt.xlabel('Close Value')
plt.ylabel('Frequency')
plt.show()