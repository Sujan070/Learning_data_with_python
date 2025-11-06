import numpy as np
import matplotlib.pyplot as plt
import random

years = [2014, 2015, 2016, 2017,
         2018, 2019, 2020, 2021]
income = [55, 56, 62, 61, 72, 72, 73, 75]

income_tics = list(range(50, 81, 2))
plt.plot(years, income)
plt.title("income of Jhon (in usd)")
plt.xlabel("Years")
plt.ylabel("Yearly Income in dollars")
plt.yticks(income_tics, [f"${x}k" for x in income_tics])
# plt.xticks(years, [f"year{x}" for x in years])
plt.show()

x = [50, 54, 65, 58, 49, 52]
y = [58, 57, 61, 64, 53, 66]
z = [46, 49, 54, 59, 51, 60]
plt.plot(x, label="fig1")
plt.plot(y, label="fig2")
plt.plot(z, label="fig3")
plt.legend()
plt.show()

x = np.arange(100)
fig, axs = plt.subplots(2,2)
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine wave")

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title("Cosine wave")

axs[1, 0].plot(x, np.random.random(100))
axs[1, 0].set_title("Log function")
plt.tight_layout()
fig.suptitle("sub plots")
plt.show()
ax = plt.axes(projection="3d")
ax.scatter(x, y, z)
plt.show()
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
z = np.sin(X) * np.cos(Y)
ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, z, cmap="Spectral")
plt.show()
h_t = [0, 0]
for _ in range(100):
    h_t[random.randint(0, 1)] += 1
    plt.bar(["heads", "tails"], h_t, color=["red", "blue"])
    plt.pause(0.002)
plt.show()
