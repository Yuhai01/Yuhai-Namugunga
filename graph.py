import matplotlib.pyplot as plt

x = [5,10,15,20,25]
y = [5.0067901611328125e-05,0.0001049041748046875,0.0002129077911376953,0.0003561973571777344,0.0006699562072753906]

plt.plot(x,y)

plt.xlabel("Number of inputs")
plt.ylabel("Running time")
plt.title("complexity")

plt.show()