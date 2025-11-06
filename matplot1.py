import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

# print(X_data, Y_data)
plt.scatter(X_data, Y_data, c="blue", marker = "*", s=120 ,alpha = 0.5)
plt.show()

years = [2006 +x for x in range(16)]
weights = [80, 85, 87, 98, 87, 87, 85, 86, 87, 88, 88, 89, 86, 85, 89, 84]
# print(len(weights))
# print(len(years))
plt.plot(years, weights)
plt.show()

x = ["c++", "python", "c#", "java", "javascript"]
y = [99, 90, 99, 85, 64]
plt.bar(x, y, color ="red", align = "edge", width=0.5, edgecolor ="green", lw=3)
plt.show()

ages = np.random.normal(20, 1.5, 1000)
print(ages)
plt.hist(ages, bins = 10, cumulative= True)
plt.show()

x = ["c++", "python", "c#", "java", "javascript"]
y = [80, 90, 93, 55, 64]
explodes = [0, 0, 0, 0.12, 0.1]
plt.pie(y, labels = x, explode= explodes, autopct="%.2f%%", pctdistance=1.35)
plt.show()

heights = np.random.normal(170, 6, 200)
plt.boxplot(heights)
plt.show()