import matplotlib.pyplot as plt
data=[1,2,35,45,5,6,8,34,23,5,44,33]
bins=[0,10,20,30,40,50]


plt.hist(data,bins=bins,color="skyblue",edgecolor="black")
plt.xlabel(" Ranges")
plt.ylabel("Frequency")
plt.title("Simple Histogram Example")
plt.show()