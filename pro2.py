import numpy as np
import matplotlib.pyplot as plt
sales=np.array([100,200,150,300,250])
print(sales)
profit=np.array([20,40,30,60,50])
print(profit)
plt.plot(sales, profit)
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Sales vs Profit')
plt.show()