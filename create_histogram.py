import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'1':698.12, '2':738.94, '4':770.95, '8':960.75, '10': 880.61}

instances = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (5, 5))
 
# creating the bar plot
plt.bar(instances, values, color ='royalblue',width = 0.5)
 
plt.xlabel("Number of Instance")
plt.ylabel("Requests per Second")
plt.title("Performance of Docker Swarm")
plt.show()