import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel (r'C:\Users\saurav\Desktop\work2.xlsx') 
df1 = df.iloc[:,0:1]
df2 = df.iloc[:,1:2]
print('Extracted from excel')
print(df)
print('First column')
print(df1)
print('Second column')
print(df2)
plt.scatter(df1,df2)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('y vs. x plot')
plt.legend('plot')
plt.show()

