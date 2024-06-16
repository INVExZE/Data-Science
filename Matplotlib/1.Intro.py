import matplotlib.pyplot as plt
x = ["C", "C++", "Java", "Python", "HTML"]
y = [90, 70, 60, 20, 87]

plt.xlabel ("Languages")
plt.ylabel ("No. Of Users")

plt.title ("Data of Active Users")


'''USE THESE INSIDE (plt.bar)'''
# Width - To Change the width of the bar graph 
# Color - To change the colour of the graph
# EdgeColor - To change the edge color of the graph
# LineWidth - To change the line with of the graph
# LineStyle - To chnage the outline style of the graph license
# Aplha - To change the opacity of the graph 

plt.bar(x, y)
plt.grid(True, zorder = 0)
plt.show()
