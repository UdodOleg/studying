from matplotlib import pyplot as plt
import random
import time
x=[]
y=[]
massive=[]
for i in range (10,100):
    for j in range (0,i):
        massive.append(random.randint(0,10000))
    start = time.time()
    massive.sort();
    end = time.time()
    massive.clear()
    x.append(i)
    y.append((end-start))
plt.plot(x,y)
plt.show()