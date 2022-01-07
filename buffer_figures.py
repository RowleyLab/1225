import numpy as np
from matplotlib import pyplot as plt
from numpy import log10 as log

pKa=4.74
dropMoles=0.001/20
xvals = np.arange(-6,+7,1)
moles=np.array([0.001,0.005,0.010])
HA=np.array([0.95,0.5,0.1,0.05])
A = np.array([0.05,0.5,0.9,0.95])
pHvals = np.zeros([3,4,13])

for i, drops in enumerate(xvals):
    for j in range(4):
        for k in range(3):
            Bmoles = (A[j]*moles[k]+drops*dropMoles)
            Amoles = (HA[j]*moles[k]-drops*dropMoles)
            if Bmoles < 0:
                pHvals[k][j][i] = -log(-Bmoles/.02)
            elif Bmoles == 0:
                pHvals[k][j][i] = -log(np.sqrt(Amoles/.02*10**-pKa))
            elif Amoles < 0:
                pHvals[k][j][i] = 14 + log(-Amoles/0.02)
            elif Amoles == 0:
                pHvals[k][j][i] = 14 + log(np.sqrt(Bmoles/.02*1e-14/10**-pKa))
            else:
                pHvals[k][j][i] = pKa + log(Bmoles/Amoles)
fig = plt.figure()
ax1 = fig.add_subplot(131)
plt.ylabel("pH")
plt.xlabel("Drops Added")
plt.title("Series A")
ax2 = fig.add_subplot(132)
plt.ylabel("pH")
plt.xlabel("Drops Added")
plt.title("Series B")
ax3 = fig.add_subplot(133)
plt.ylabel("pH")
plt.xlabel("Drops Added")
plt.title("Series C")
for i in range(4):
    ax1.scatter(xvals, pHvals[0][i], label="Buffer {}".format(i+1))
    ax2.scatter(xvals, pHvals[1][i], label="Buffer {}".format(i+1))
    ax3.scatter(xvals, pHvals[2][i], label="Buffer {}".format(i+1))
ax1.set_ylim(1,13)
ax1.legend()
ax2.set_ylim(1,13)
ax2.legend()
ax3.set_ylim(1,13)
ax3.legend()
plt.show()


