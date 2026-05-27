#Boyle's Law(P~1/V)

import matplotlib.pyplot as plt
import numpy as np

pre = np.array([1,2,4,6,8,10])
vol = np.array([24.62,12.31,6.15,4.10,3.08,2.46])

plt.title("Boyle's Law P!=V")
plt.xlabel("Pressure")#lable()
plt.ylabel("Volume")

plt.plot(pre,vol,marker="o",ms=5,mec="r",mfc="r")
plt.show()

#Charles's Law(V=T)

tem = np.array([200,300,400,500,600])
vol = np.array([24.62,32.82,41.03,53.08,62.46])

plt.title("Charles's Law T=V")
plt.xlabel("Temperature")#lable()
plt.ylabel("Volume")

plt.plot(tem,vol,marker="o",ms=5,mec="k",mfc="r")
plt.show()

#Lussac's Law(P=T)

pr = np.array([0.73,1.10,1.47,1.83,2.21])
tem = np.array([200,300,400,500,600])

plt.title("Lussac's Law P=T")
plt.xlabel("Pressure")#lable()
plt.ylabel("Temperature")


plt.plot(pr,tem,marker="o",ms=5,mec="y",mfc="r")
plt.show()

#Avogadro's Law(V=n)

nom = np.array([1,2,3,4,5])
vol = np.array([24.62,32.82,41.03,53.08,62.46])

plt.title("Avogadro's Law n=V")
plt.xlabel("Numbers of moles")#lable()
plt.ylabel("Volume")

plt.plot(nom,vol,marker="o",ms=5,mec="g",mfc="r")
plt.show()

