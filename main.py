import numpy as np
import matplotlib.pyplot as plt

filename = "" # path + filename
reName = filename.split(".txt")[0]
raw = np.loadtxt(filename)
jitters = []
for i in range(1000, len(raw)):
    temp = ( raw[i] - raw[1000] - 0.0001 * (i-1000) ) * 1000000
    jitters.append(temp)


mean = np.mean(jitters)
var = np.var(jitters)
max = np.max(jitters)
min = np.min(jitters)

with open(reName+"_cal.txt", mode="w+") as f:
    f.write("mean: {:.3f}\nvar: {:.6f}\nmax: {:.3f}\nmin: {:3f}".format(mean, var, max, min))

fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(1,1,1)
# ax1.title(reName)
# ax1.set_title(reName)
ax1.set_xlabel("cycle")
# plt.xticks(np.arange(0,  250000, 1000000))
ax1.set_ylabel("micro second")
ax1.grid()
ax1.plot(jitters)

fig.savefig(reName+".png")
# fig.show()