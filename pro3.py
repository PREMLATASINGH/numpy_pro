import numpy as np
import matplotlib.pyplot as plt
days=np.array([1,2,3,4,5,6,7])
temperature=np.array([30,40,50,60,70,80,90])
plt.plot(days, temperature)
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Temperature over Days')
plt.show()
plt.scatter(days, temperature, color='red', marker='x', s=100)
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Temperature over Days')
plt.show()