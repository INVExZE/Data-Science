import matplotlib.pyplot as plt

x = [ 1, 2, 3, 4, 5 , 6 , 7 , 8, 9, 10]
y = [5, 1, 9, 4, 9, 2, 6, 8 , 1, 3 ]

colors = ["r", "y", "b", "g", "r", "y", "b", "g", "r", "y"]
sizes = [100, 200, 150, 200, 100, 300, 250, 50, 150, 100 ]
plt.scatter(x, y, c = colors, s = sizes)

plt.xlabel ("Number")
plt.ylabel ("No of Parcels")
plt.title ("Data")

plt.scatter(x, y)
plt.show()

