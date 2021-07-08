import numpy as np
import matplotlib.pyplot as plt

print("** Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. What command do you use if you aren't using the jupyter notebook?**")
print("plt.show()")
print()
x = np.arange(0, 100)
y = x*2
z = x**2

'''
## Exercise 1

** Follow along with these steps: **
* ** Create a figure object called fig using plt.figure() **
* ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
* ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**

fig = plt.figure()

ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,'blue')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("title")
'''
'''
## Exercise 2
** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**


fig2 = plt.figure()

ax1 = fig2.add_axes([0.1,0.1,0.8,0.8])
ax2 = fig2.add_axes([0.3,0.5,.2,.2])

ax1.plot(x,z,'r')
ax1.set_ylabel('Z')
ax1.set_xlabel('X')
ax2.plot(x,y,'r')
ax2.set_title('zoom')
ax2.set_ylabel('Y')
ax2.set_xlabel('X')

plt.show()
'''
'''
#Exercise 3

fig2 = plt.figure()

ax1 = fig2.add_axes([0.1,0.1,0.8,0.8])
ax2 = fig2.add_axes([0.3,0.5,.2,.2])

ax1.plot(x,z,'r')
ax1.set_ylabel('Z')
ax1.set_xlabel('X')
ax2.plot(x,y,'r')
ax2.set_title('zoom')
ax2.set_ylabel('Y')
ax2.set_xlabel('X')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)

plt.tight_layout()
plt.show()
'''

#Exercise 4

fig, axes = plt.subplots(1,2, figsize=(8,4))

axes[0].plot(x,y,'red',linewidth=0.5,linestyle="--")
axes[1].plot(x,z,'green',linewidth=2,linestyle=":")

plt.tight_layout()
plt.show()
