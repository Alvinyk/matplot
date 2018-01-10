import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

#plt.scatter(x_values,y_values,edgecolor='none',s=20)
#plt.scatter(x_values,y_values,c='red',s=20)

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
            edgecolors='none',s=4)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)

#plt.show()
plt.savefig('../img/squares_plot.png',bbox_inches='tight')
