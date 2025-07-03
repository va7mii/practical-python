import matplotlib.pyplot as plt
import numpy as np
import random
import math

num_walks = 2**16

xpoints = np.arange(0,num_walks)
ypoints = np.empty(num_walks)

cur_spot = 0


# Random walk scenario
for points in xpoints:
    
    ypoints[points] = cur_spot
    
    rand = random.randint(0,1)
    
    if (rand == 1):
        cur_spot += 1
    else:
        cur_spot -= 1
    
zpoints = zip(xpoints,ypoints)
keys = dict(zpoints)

print(keys)
    
    
    
    
    


plt.plot(xpoints, ypoints)
plt.show()