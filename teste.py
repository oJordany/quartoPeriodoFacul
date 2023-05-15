import matplotlib.pyplot as plt
import numpy as np

#define figure
fig = plt.figure()
#add subplots
fig.add_subplot(311).set_title('311')
fig.add_subplot(312).set_title('312')
fig.add_subplot(325).set_title('325')
fig.add_subplot(326).set_title('326')

#display plots
plt.show()