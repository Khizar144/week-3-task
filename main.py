import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# # x axis
# x=[1,2,3]
# #y axis
# y=[2,4,1]
# # plot the grph
# plt.plot(x,y)
# plt.xlabel("x-Axix")
# plt.ylabel("y-Axix")
# plt.title("Sample graph")
# plt.show()

x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

plt.xlabel("x-Axix")
plt.ylabel("y-Axix")

plt.title('Two or more lines with different widths and colors with suitable legends ')

plt.plot(x1,y1, color='blue', linewidth=3,label="Line1-width-3")
plt.plot(x2,y2, color='red', linewidth=5,label="Line2-width-5")
plt.legend()
plt.show()


# Write a Python program to plot two or more lines and set the line markers. The code snippet gives
# the output shown in the following screenshot:

# x axis
x = [1,4,5,6,7]
# y axis
y = [2,6,3,6,3]


plt.plot(x,y, color='red',linestyle='dashdot',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
plt.show()


languages = ['java','Python', 'PHP', 'javaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Plotting the horizontal bar chart
plt.barh(languages, popularity, color='green')
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')
plt.grid(axis='x')
plt.show()

columns=['a','b','c','d','e']
a=np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
df=pd.DataFrame(a,columns=columns)

df.plot(kind='bar')
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()