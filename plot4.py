import numpy as np
import matplotlib.pyplot as plt
course=np.array(['c','c++','java','python'])
girl=np.array([40,50,45,20])
boy=np.array([45,43,37,50])
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.5,0.5])
ax.bar(course,girl,color='red',width=.30)
ax.bar(course,boy,color='yellow',bottom=girl,width=.30)
ax.legend(['girl','boy'])
plt.show()
